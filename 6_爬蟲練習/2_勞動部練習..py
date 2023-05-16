import requests, codecs
#需使用request模組來取得網頁資訊

r1 = requests.get("https://www.mol.gov.tw/", 
                  headers= {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}, 
                  )
print(r1)
#get為呼叫方法，後面要接網址與標頭

r1 = requests.get("https://www.mol.gov.tw/media/dh5j5jhr/recommend_icon17.png")
#下載png / jpg圖檔的方法

with codecs.open("recommend_icon17.png","wb") as f:
  f.write(r1.content)
#儲存檔案為"recommend_icon17.png"

with codecs.open("內容.txt","wb") as f:
  f.write(r1.content)
  
r2 = requests.post("http://teaching.bo-yuan.net/?ex=logout",headers={
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "referer" : "http://teaching.bo-yuan.net/",
    "cookie" : "PHPSESSID=5s2gvcfaa0no36pq9enojssjcg"
    #chrome開發人員選項中"標頭 - 回應標頭"
},params = {
    "ex" : "logout"})
    #chrome開發人員選項中"酬載 - 查詢字串參數"  #登出