import csv
import codecs
import io
import requests

# with codecs.open("1.csv","r") as f:
#     d = list(csv.reader(f))
#     print(d)

# 使用 codecs 模組中的 open() 方法，並以讀取模式 ("r") 開啟。接著使用 csv 模組中的 reader() 方法將檔案讀取為一個清單，並將其存入變數 d 中。最後將 d 印出。

r1 = requests.get("https://data.taipei/api/dataset/46e781dd-4b90-411f-bafe-7f6226587e0a/resource/d7eb121c-dcd7-43b5-bbb7-359d5ea7905d/download",
                  headers={
                      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"},
                  )

r1.encoding = "big5"  # 中文常用big5 英文數字用UTC-8

f = io.StringIO(r1.text)
d = list(csv.reader(f))

txt = ""

for i in range(len(d)):
    txt = txt + ",".join(d[i])+"\n"

print(txt)
