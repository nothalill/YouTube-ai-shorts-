
import whisper
import os

def generate_subtitles(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    srt_path = video_path.replace('.mp4', '.srt')
    with open(srt_path, 'w', encoding='utf-8') as f:
        for i, seg in enumerate(result['segments']):
            f.write(f"{i+1}\n{seg['start']} --> {seg['end']}\n{seg['text']}\n\n")
    return video_path
