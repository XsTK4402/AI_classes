import requests,codecs

r1 = requests.post("http://teaching.bo-yuan.net/?ex=login",headers={
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "referer" : "http://teaching.bo-yuan.net/",
    "cookie" : "PHPSESSID=5s2gvcfaa0no36pq9enojssjcg"
    #chrome開發人員選項中"標頭 - 回應標頭"
},params = {
    "ex" : "login"
    #chrome開發人員選項中"酬載 - 查詢字串參數"
},data = {
    "ex[class]" : "6400867314b39",
    "ex[username]" : "18常庭豪",
    "ex[password]" : "324804"})
    #chrome開發人員選項中"酬載 - 表單資料"

print(r1)

with codecs.open("內容.txt","wb") as f:
  f.write(r1.content)
  