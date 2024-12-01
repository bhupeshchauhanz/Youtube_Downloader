import yt_dlp
import os

def download_thumbnail(url):
    dest_folder = input("Enter the destination folder path: ")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    ydl_opts = {
        'format': 'best',
        'writethumbnail': True,
        'outtmpl': os.path.join(dest_folder, '%(title)s_thumbnail.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_thumbnail('https://www.youtube.com/watch?v=VIDEO_ID')
