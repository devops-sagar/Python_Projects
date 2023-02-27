from pytube import YouTube
import os

print(os.getcwd())
YouTube('https://youtu.be/dva0jOeov7I').streams().first().download()
yt = YouTube('https://www.youtube.com/watch?v=dva0jOeov7I')
yt.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download()