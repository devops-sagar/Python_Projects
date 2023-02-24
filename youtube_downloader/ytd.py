from pytube import YouTube

YouTube('https://youtu.be/XKtiIP_-dFE').streams().first().download()
yt = YouTube('https://www.youtube.com/watch?v=XKtiIP_-dFE')
yt.streams.filter(progressive = True, file_extension = 'mp4').order_by('resolution').desc().first().download()