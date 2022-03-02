from pytube import Playlist
pl = Playlist("https://www.youtube.com/watch?v=O6P86uwfdR0&list=PLZlA0Gpn_vH8EtggFGERCwMY5u5hOjf-h")
print(pl.title)

for video in pl.videos:
    video.streams.first().download()
print("Downloaded Successfully")