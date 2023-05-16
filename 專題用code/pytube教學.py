from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=KOkI80Z3H2s&ab_channel=TheEntertainmentAnalyst')   

print(yt.title)           # 影片標題
print(yt.length)          # 影片長度 ( 秒 )
print(yt.author)          # 影片作者
print(yt.channel_url)     # 影片作者頻道網址
print(yt.thumbnail_url)   # 影片縮圖網址
print(yt.views)           # 影片觀看數
#print(yt.streams.all())  # 支援哪些畫質

yt.streams.filter().get_highest_resolution().download(filename = "marvel_trailor\marvel3.mp4")

print('ok!')