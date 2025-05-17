
import yt_dlp
import os

CHANNELS = [
    'https://www.youtube.com/@MrBeast',
    'https://www.youtube.com/@PewDiePie',
    'https://www.youtube.com/@emmachamberlain',
    'https://www.youtube.com/@markiplier',
    'https://www.youtube.com/@mkbhd'
]

def download_latest_videos():
    os.makedirs("downloads", exist_ok=True)
    ydl_opts = {
        'outtmpl': 'downloads/%(uploader)s_%(id)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'download_archive': 'downloaded.txt'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        paths = []
        for url in CHANNELS:
            info = ydl.extract_info(url + '/videos', download=True)
            if 'entries' in info:
                for entry in info['entries'][:1]:
                    paths.append(ydl.prepare_filename(entry))
        return paths
