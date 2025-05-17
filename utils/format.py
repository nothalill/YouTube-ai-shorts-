
from moviepy.editor import VideoFileClip
import os

def format_for_shorts(video_path):
    clip = VideoFileClip(video_path)
    clip_resized = clip.resize(height=1080)
    final = clip_resized.crop(width=608, x_center=clip_resized.w/2)
    out_path = "shorts/" + os.path.basename(video_path)
    os.makedirs("shorts", exist_ok=True)
    final.write_videofile(out_path, codec="libx264")
    return out_path
