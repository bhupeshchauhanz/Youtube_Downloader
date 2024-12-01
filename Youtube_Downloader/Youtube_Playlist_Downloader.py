import yt_dlp
import os

def download_playlist():
    url = input("Enter the YouTube playlist URL: ")
    dest_folder = input("Enter the destination folder path: ")

    # Validate the URL
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' not in info:  # Check if it's a playlist
                raise yt_dlp.utils.DownloadError("Not a playlist URL")
    except yt_dlp.utils.DownloadError:
        print("Eror Detected Please Provide valid Link.")
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(dest_folder, '%(playlist_title)s', '%(title)s.%(ext)s'),
        'noplaylist': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Run the function
download_playlist()
