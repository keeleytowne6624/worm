from pytube import YouTube

def download_video(url):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the highest resolution stream
        stream = video.streams.get_highest_resolution()

        # Download the video
        stream.download()
        print("Video downloaded successfully!")

    except Exception as e:
        print("Error:", str(e))

# Example usage
video_url = "https://www.youtube.com/watch?v=J9iM5qJL1j0&ab_channel=GrantCollins"
download_video(video_url)
