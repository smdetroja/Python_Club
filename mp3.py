from pydub import YouTubeAudio

# URL of the video to download
url = 'https://www.youtube.com/watch?v=--eH76tgoNw'

# Download the audio
audio = YouTubeAudio(url).download()

# Set the audio format and save
audio.export("song.mp3", format="mp3")
