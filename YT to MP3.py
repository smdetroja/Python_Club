# importing packages
from pytube import YouTube
import os

TotalNo = eval(input("Enter Number of URL: "))

# check for each URL
for i in range(0,TotalNo):
    
    # url input from user
    yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # destination to save file

    destination = 'E:\Music'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")


