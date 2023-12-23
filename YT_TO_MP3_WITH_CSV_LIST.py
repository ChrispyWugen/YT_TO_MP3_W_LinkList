# importing packages 
from pytube import YouTube 
import os 

#read csv data list
csvdatei = open('LinkList.txt','r')
for row in csvdatei:
    print("Current URL: " + row)
    yt = YouTube(str(row))


    # extract only audio 
    video = yt.streams.filter(only_audio=True).first() 

    # destination to save file 
    destination = '.'

    # download the file 
    out_file = video.download(output_path=destination) 

    # save the file 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    
    # result of success 
    print(yt.title + " has been successfully downloaded.")