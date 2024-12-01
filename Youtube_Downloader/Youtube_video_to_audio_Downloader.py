import yt_dlp

def download_audio(url, destination_folder):
    # Validate the URL
    try:
        with yt_dlp.YoutubeDL() as ydl:
            ydl.extract_info(url, download=False)  # Check if the link is valid
    except yt_dlp.utils.DownloadError:
        print("Eror Detected Please Provide valid Link.")
        return

    # Define download options
    ydl_opts = {
        'format': 'bestaudio/best',  # Get the best audio format available
        'outtmpl': f'{destination_folder}/%(title)s.%(ext)s',  # Output file template
        'noprogress': True,  # Disable progress bar
        'postprocessors': [],  # Disable post-processing (no format conversion)
        'nocheckcertificate': True,  # For SSL issues, optional
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Replace with your YouTube video URL and destination folder
video_url = input("Enter the YouTube video URL: ")
destination = input("Enter the destination folder path: ")
download_audio(video_url, destination)
