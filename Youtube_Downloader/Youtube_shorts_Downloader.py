import yt_dlp
import os

def download_youtube_shorts(url):
    dest_folder = input("Enter the destination folder path: ")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(dest_folder, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_youtube_shorts('https://www.youtube.com/shorts/VIDEO_ID')
