from flask import Flask, request, jsonify, render_template
from moviepy.editor import VideoFileClip
import os
import speech_recognition as sr
from googletrans import Translator
import yt_dlp
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        audio.close()
        video.close()
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        raise

def transcribe_audio(audio_path):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='en-US')
        return text
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        raise

def translate_text(text, dest_lang):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=dest_lang).text
        return translated_text
    except Exception as e:
        logging.error(f"Error translating text: {e}")
        raise

def download_youtube_video(url, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_file_path = ydl.prepare_filename(info_dict)
            audio_file_path = os.path.splitext(audio_file_path)[0] + '.wav'
        return audio_file_path
    except Exception as e:
        logging.error(f"Error downloading YouTube video: {e}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_video_to_text():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        video_file = request.files['video']
        video_path = os.path.join('videos', video_file.filename)
        audio_path = os.path.join('audios', os.path.splitext(video_file.filename)[0] + '.wav')
        
        video_file.save(video_path)
        
        extract_audio(video_path, audio_path)
        text = transcribe_audio(audio_path)
        translated_text_ta = translate_text(text, 'ta')
        translated_text_hi = translate_text(text, 'hi')
        
        os.remove(video_path)
        os.remove(audio_path)
        
        return jsonify({'text': text, 'translated_text_ta': translated_text_ta, 'translated_text_hi': translated_text_hi})
    except Exception as e:
        logging.error(f"Error processing video: {e}")
        return jsonify({'error': 'Error processing video'}), 500

@app.route('/convert-link', methods=['POST'])
def convert_youtube_to_text():
    try:
        data = request.get_json()
        url = data.get('url')
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        audio_path = download_youtube_video(url, 'audios')
        text = transcribe_audio(audio_path)
        translated_text_ta = translate_text(text, 'ta')
        translated_text_hi = translate_text(text, 'hi')
        
        os.remove(audio_path)
        
        return jsonify({'text': text, 'translated_text_ta': translated_text_ta, 'translated_text_hi': translated_text_hi})
    except Exception as e:
        logging.error(f"Error processing YouTube link: {e}")
        return jsonify({'error': 'Error processing YouTube link'}), 500

if __name__ == '__main__':
    os.makedirs('videos', exist_ok=True)
    os.makedirs('audios', exist_ok=True)
=======
from flask import Flask, request, jsonify, render_template
from moviepy.editor import VideoFileClip
import os
import speech_recognition as sr
from googletrans import Translator
import yt_dlp
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_audio(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        audio.close()
        video.close()
    except Exception as e:
        logging.error(f"Error extracting audio: {e}")
        raise

def transcribe_audio(audio_path):
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='en-US')
        return text
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        raise

def translate_text(text, dest_lang):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=dest_lang).text
        return translated_text
    except Exception as e:
        logging.error(f"Error translating text: {e}")
        raise

def download_youtube_video(url, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_file_path = ydl.prepare_filename(info_dict)
            audio_file_path = os.path.splitext(audio_file_path)[0] + '.wav'
        return audio_file_path
    except Exception as e:
        logging.error(f"Error downloading YouTube video: {e}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_video_to_text():
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        video_file = request.files['video']
        video_path = os.path.join('videos', video_file.filename)
        audio_path = os.path.join('audios', os.path.splitext(video_file.filename)[0] + '.wav')
        
        video_file.save(video_path)
        
        extract_audio(video_path, audio_path)
        text = transcribe_audio(audio_path)
        translated_text_ta = translate_text(text, 'ta')
        translated_text_hi = translate_text(text, 'hi')
        
        os.remove(video_path)
        os.remove(audio_path)
        
        return jsonify({'text': text, 'translated_text_ta': translated_text_ta, 'translated_text_hi': translated_text_hi})
    except Exception as e:
        logging.error(f"Error processing video: {e}")
        return jsonify({'error': 'Error processing video'}), 500

@app.route('/convert-link', methods=['POST'])
def convert_youtube_to_text():
    try:
        data = request.get_json()
        url = data.get('url')
        if not url:
            return jsonify({'error': 'No URL provided'}), 400
        
        audio_path = download_youtube_video(url, 'audios')
        text = transcribe_audio(audio_path)
        translated_text_ta = translate_text(text, 'ta')
        translated_text_hi = translate_text(text, 'hi')
        
        os.remove(audio_path)
        
        return jsonify({'text': text, 'translated_text_ta': translated_text_ta, 'translated_text_hi': translated_text_hi})
    except Exception as e:
        logging.error(f"Error processing YouTube link: {e}")
        return jsonify({'error': 'Error processing YouTube link'}), 500

if __name__ == '__main__':
    os.makedirs('videos', exist_ok=True)
    os.makedirs('audios', exist_ok=True)
>>>>>>> cfbb873a833b472aed989cfce688a408eaa2904d
    app.run(debug=True)
