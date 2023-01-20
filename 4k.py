from pytube import YouTube

# URL of the video to download
url = 'https://youtu.be/LXb3EKWsInQ'

# Create a YouTube object
yt = YouTube(url)

# Get the highest resolution video available
video = yt.streams.filter(resolution='2160p').first()

# Download the video
video.download()
