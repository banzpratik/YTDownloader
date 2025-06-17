from yt_dlp import YoutubeDL

def download_video(url):
    ydl_opts = {'format': 'best'}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
