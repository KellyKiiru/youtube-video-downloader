from tokenize import maybe
from pytube import YouTube

"""
Replace url with your preferred video url then run the script.
The video will be downloaded in the same folder that contains this file
"""

url = 'https://www.youtube.com/watch?v=UprcpdwuwCg&list=RDUKunvvN2iCk&index=15'

my_video = YouTube(url)


print(my_video.title)

my_video = my_video.streams.get_highest_resolution()
    
my_video.download()
