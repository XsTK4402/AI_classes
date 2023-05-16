import requests, json

r1 = requests.get("https://datacenter.taichung.gov.tw/swagger/OpenData/30a65071-1066-40be-9ff8-906057fb7658", params = {
    "origin" : "",
    "lang" : "zh-tw",
    "branch" : "home"
})

# print(r1.json())

d = json.loads(r1.text)

for i in d :
    print(i["一次安家費件戶數"])
