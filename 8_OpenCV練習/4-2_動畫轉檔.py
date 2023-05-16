# python檔案加入音軌
import IPython.display as dp
import codecs, base64

with codecs.open("C:/Users/Matthew/Desktop/python/data/1.mp4", "rb") as f:
    d = base64.b64encode(f.read()).decode()
    
dp.HTML(f'<video src="data:video/mp4:base64, {d}" controls />')