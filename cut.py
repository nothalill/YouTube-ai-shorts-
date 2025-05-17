
import subprocess
import os

def detect_scenes(video_path):
    scene_folder = "scenes/"
    os.makedirs(scene_folder, exist_ok=True)
    subprocess.run([
        "scenedetect", "-i", video_path,
        "-o", scene_folder,
        "detect-content", "list-scenes", "split-video"
    ])
    return [os.path.join(scene_folder, f) for f in os.listdir(scene_folder) if f.endswith('.mp4')]
