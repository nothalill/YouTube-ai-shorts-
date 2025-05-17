
from flask import Flask, request, jsonify
from utils.download import download_latest_videos
from utils.cut import detect_scenes
from utils.subtitles import generate_subtitles
from utils.format import format_for_shorts
from utils.upload import upload_video
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Backend YouTube AI Shorts работает!"})

@app.route('/process_videos', methods=['POST'])
def process_videos():
    try:
        video_paths = download_latest_videos()
        uploaded_videos = []

        for path in video_paths:
            scenes = detect_scenes(path)
            for scene_path in scenes:
                sub_path = generate_subtitles(scene_path)
                final_path = format_for_shorts(sub_path)
                video_id = upload_video(final_path)
                uploaded_videos.append({
                    "video_path": final_path,
                    "youtube_id": video_id
                })

        return jsonify({
            "message": "Видео обработаны и загружены",
            "uploaded": uploaded_videos
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
