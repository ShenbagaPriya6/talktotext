# Video to Text and Translation Web Application
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

## 🚀 Prerequisites

- Python 3.6+
- Flask
- MoviePy
- SpeechRecognition
- googletrans
- yt-dlp
- FFmpeg

## 📥 Installation

**Clone the Repository**:
   ```bash
   git clone https://github.com/ShenbagaPriya6/talktotext.git
   cd video-to-text-translation
   ```

 **Ensure FFmpeg is Installed**: Make sure FFmpeg is available in your system's PATH.

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

## 💖 Acknowledgements

Special thanks to the developers and maintainers of the libraries and tools used in this project, including Flask, MoviePy, SpeechRecognition, googletrans, yt-dlp, and FFmpeg.

---

## 🖼️ Screenshots

### Home Page
![Home Page](images/homepage.png)

### Translated Text
![Translated Text](images/translated_text.png)


