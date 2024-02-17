from flask import Flask, render_template, request
import requests
import io
import os
import uuid
import json
import time
from PIL import Image, UnidentifiedImageError
import threading

app = Flask(__name__)

def save_to_json(data):
    json_file = 'conversation.json'
    if not os.path.exists(json_file):
        with open(json_file, 'w') as f:
            json.dump([], f)
    with open(json_file, 'r+') as f:
        conversations = json.load(f)
        conversations.append(data)
        f.seek(0)
        json.dump(conversations, f, indent=4)

def load_from_json():
    json_file = 'conversation.json'
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            return json.load(f)
    return []

def upload_image_to_imgbb(image_data, image_path):
    api_url = "https://api.imgbb.com/1/upload"
    params = {
        "expiration": "5000",  
        "key": os.environ.get('IMGBB_API_KEY')
    }
    response = requests.post(api_url, params=params, files={"image": image_data})
    if response.status_code == 200:
        json_response = response.json()
        uploaded_image_url = json_response['data']['url']
        # Delete the locally saved image
        os.remove(image_path)
        return uploaded_image_url
    else:
        print("Error uploading image to imgbb:", response.status_code)
        return None

def generate_image(input_text, api_url):
    headers = {"Authorization": f"Bearer {os.environ.get('GENERATE_IMAGE_TOKEN')}"}
    
    start_time = time.time()  # Start time for measuring generation time
    
    try:
        response = requests.post(api_url, headers=headers, json={"inputs": input_text})
        image_bytes = response.content
        image = Image.open(io.BytesIO(image_bytes))
        unique_filename = str(uuid.uuid4()) + '.png'
        image_path = os.path.join('static', unique_filename)
        image.save(image_path)
        
        # Upload the generated image to imgbb.com using threading
        uploaded_image_url = upload_image_to_imgbb(image_bytes, image_path)
        
        end_time = time.time()  # End time for measuring generation time
        generate_time = round(end_time - start_time, 2)  # Calculate generation time
        
        return uploaded_image_url, generate_time
    
    except UnidentifiedImageError as e:
        print(f"Error generating image: {e}")
        return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        api_url = request.form.get('api_select')
        image_url, generate_time = generate_image(input_text, api_url)
        
        if image_url is not None and generate_time is not None:
            conversation_data = {
                'id': str(uuid.uuid4()),
                'input_text': input_text,
                'image_url': image_url,  # Store the uploaded image URL instead of local path
                'generate_time': generate_time,
                'timestamp': time.time()
            }
            save_to_json(conversation_data)
        
        return render_template('index.html', conversation=load_from_json())

    return render_template('index.html', conversation=load_from_json())

if __name__ == '__main__':
    app.run(debug=True)
