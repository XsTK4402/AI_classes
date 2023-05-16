import requests

r1 = requests.get("https://udn.com/api/more",params = {
    "page" : "22",
    "id":"",
    "channelId":"1",
    "cate_id":"0",
    "type":"breaknews",
    "totalRecNo":"26304"
})

r1 = r1.json()

for i in range(1,6,1):
    print(r1["lists"][i]["time"]["date"])

