import requests

r1 = requests.post("http://teaching.bo-yuan.net/test/requests/",headers={
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding" : "gzip, deflate",
    "Accept-Language" : "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control" : "max-age=0",
    "Connection" : "keep-alive",
    "cookie" : "PHPSESSID=5s2gvcfaa0no36pq9enojssjcg",
    "Host" : "teaching.bo-yuan.net",
    "Upgrade-Insecure-Requests" : "1",
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"},
params = {
    "action" : "0000",
     },
data = {
    "id" : "0000",
    "name" : "18",
    "address" : "172.105.216.56"
})

print(r1.text)
