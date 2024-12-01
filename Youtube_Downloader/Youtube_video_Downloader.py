import yt_dlp
import os

def download_video():
    url = input("Enter the YouTube video URL: ")
    dest_folder = input("Enter the destination folder path: ")

    # Validate the URL
    try:
        with yt_dlp.YoutubeDL() as ydl:
            ydl.extract_info(url, download=False)  # Check if the link is valid
    except yt_dlp.utils.DownloadError:
        print("Eror Detected Please Provide valid Link.")
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(dest_folder, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Run the function
download_video()
