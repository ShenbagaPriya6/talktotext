# Video to Text and Translation Web Application

![Logo](static/logo.png) <!-- Add your logo here -->

## 🎬 Overview

Welcome to the Video to Text and Translation Web Application! This innovative web app allows you to:

- 📹 Upload videos or provide YouTube links
- 🔊 Extract audio from videos
- 📝 Transcribe audio to text
- 🌐 Translate transcribed text into Tamil and Hindi

The application supports various video formats and ensures efficient management of temporary files, making it user-friendly and highly functional.

## ✨ Features

- 📁 **Upload Videos**: Easily upload your video files.
- 🔗 **YouTube Links**: Provide YouTube links for direct processing.
- 🎧 **Audio Extraction**: Extract audio from your videos seamlessly.
- ✍️ **Transcription**: Convert audio to text accurately.
- 🌏 **Translation**: Translate text into Tamil and Hindi.
- 📦 **File Management**: Efficient handling of temporary files.
- ⚙️ **Multi-format Support**: Compatible with various video formats.

## 🚀 Prerequisites

- Python 3.6+
- Flask
- MoviePy
- SpeechRecognition
- googletrans
- yt-dlp
- FFmpeg

## 📥 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/video-to-text-translation.git
   cd video-to-text-translation
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure FFmpeg is Installed**: Make sure FFmpeg is available in your system's PATH.

## 🛠️ Usage

1. **Start the Flask Application**:
   ```bash
   python app.py
   ```

2. **Open Your Browser**: Navigate to `http://127.0.0.1:5000`.

3. **Interact with the App**: Upload a video or provide a YouTube link to convert the video to text and translate the text into Tamil and Hindi.

## 📂 File Structure

- `app.py`: Main application file with Flask routes and logic.
- `templates/index.html`: HTML template for the web interface.
- `requirements.txt`: List of required Python packages.
- `static/`: Directory for static files (CSS, JS, images).
- `videos/`: Directory for temporarily storing uploaded videos.
- `audios/`: Directory for temporarily storing extracted audio files.

## 🔄 Routes

- `/`: Home page for uploading videos or providing YouTube links.
- `/convert`: POST endpoint for video file upload and conversion.
- `/convert-link`: POST endpoint for YouTube link conversion.

## ⚠️ Error Handling

The application includes robust error handling for:

- Missing video file or URL in the request
- Errors during video re-encoding and audio extraction
- Errors during audio transcription
- Errors during text translation

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss any changes or improvements.

## 📜 License

This project is licensed under the MIT License.

## 💖 Acknowledgements

Special thanks to the developers and maintainers of the libraries and tools used in this project, including Flask, MoviePy, SpeechRecognition, googletrans, yt-dlp, and FFmpeg.

---

## 🖼️ Screenshots

### Home Page
![Home Page](static/homepage.png)

### Translated Text
![Translated Text](static/translated_text.png)

Feel free to customize this README to match your project's specifics and requirements.
