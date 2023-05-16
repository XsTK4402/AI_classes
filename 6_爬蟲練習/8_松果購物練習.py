import requests
from prettytable import PrettyTable

r1 = requests.get("https://xapi.pcone.com.tw/search/commodities", headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'},
    params={
    "site": "pcone",
    "direction": "asc",
    "page": "1",
    "q": input("關鍵字："),
    "sorting": "default",
    "device": "desktop",
    "aid": "null"
})

r1 = r1.json()
x = PrettyTable()

for i in range(1, 21, 1):
    x.field_names = ["商品名稱", "價格"]
    x.add_row([r1["data"]["commodities"][i]["name"], r1["data"]["commodities"][i]["price"]])
    x.align["商品名稱"] = "l"
    x.align["價格"] = "l"


print(x)
