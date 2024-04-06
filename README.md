# HF_GenAPI_Website_001

---
## Live at:
https://degozaru3.pythonanywhere.com/
---

This Flask application generates images based on input text using various AI models and uploads them to ImgBB for sharing. It provides a simple web interface for users to input text and select the desired AI model for image generation.

## Features

- Generates images based on user input text using AI models.
- Supports multiple AI models for image generation.
- Uploads generated images to ImgBB for easy sharing.
- Displays generated images and conversation history in a web interface.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/SSL-ACTX/HF_GenAPI_Website_001.git
    ```

2. Navigate to the project directory:

    ```
    cd HF_GenAPI_Website_001
    ```

3. Create a virtual environment (optional but recommended):

    ```
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On macOS and Linux:

        ```
        source venv/bin/activate
        ```

    - On Windows:

        ```
        venv\Scripts\activate
        ```

5. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

## Configuration

Before running the application, you need to set up the following environment variables:

- **IMGBB_API_KEY**: Your ImgBB API key for uploading images.
- **GENERATE_IMAGE_TOKEN**: Authorization token for accessing the image generation service.

You can set these environment variables in your local environment or use a `.env` file in the project directory.

Example `.env` file:

```
IMGBB_API_KEY=your_imgbb_api_key
GENERATE_IMAGE_TOKEN=your_generate_image_token
```

## Usage

1. Start the Flask application:

    ```
    python app.py
    ```

2. Open your web browser and go to `http://localhost:5000` to access the application.

3. Enter your text input in the provided form and select the desired AI model.

4. Click on the "Generate Image" button to generate the image.

5. The generated image will be displayed on the webpage, and the conversation history will be updated accordingly.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
