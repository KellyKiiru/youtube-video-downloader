from pytube import YouTube

"""
Replace url with your preferred video url then run the script.
The video will be downloaded in the same folder that contains this file.
Make sure to use the correct python interpreter for the project
"""

url = 'https://www.youtube.com/watch?v=CTpxQVUEMeI'

my_video = YouTube(url)


print(my_video.title)

my_video = my_video.streams.get_highest_resolution()
    
my_video.download()