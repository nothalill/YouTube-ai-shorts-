
from utils.download import download_latest_videos
from utils.cut import detect_scenes
from utils.subtitles import generate_subtitles
from utils.format import format_for_shorts
from utils.upload import upload_video
import os

def main():
    video_paths = download_latest_videos()
    for path in video_paths:
        scenes = detect_scenes(path)
        for scene_path in scenes:
            sub_path = generate_subtitles(scene_path)
            final_path = format_for_shorts(sub_path)
            upload_video(final_path)

if __name__ == "__main__":
    main()
