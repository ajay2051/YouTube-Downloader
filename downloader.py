from pytube import YouTube

url = "https://www.youtube.com/watch?v=8XrRV4Ydfwk"

my_video = YouTube(url)

# For Video Title
print(my_video.title)

#For Video Thumbnail
print(my_video.thumbnail_url)
#Download Video Options
videos = my_video.streams.all()
# For Audio Only
# videos = my_video.streams.filter(only_audio=True)
video = list(enumerate(videos))
for v in video:
    print(v)
opt = int(input("Enter Option No: "))
videos[opt].download()
print("Video Downloaded Successfully")