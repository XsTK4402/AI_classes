import requests
from prettytable import PrettyTable

a = input("關鍵字：")
page = 1
pageview = True

while pageview == True:
    r1 = requests.get("https://ecshweb.pchome.com.tw/search/v3.3/all/results", headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'},
    params={
    "q" : a,
    "page" : page,
    "sort" : "sale/dc",
    })

    r1 = r1.json()
    x = PrettyTable()

    for i in range(0, len(r1["prods"]), 1):
        x.field_names = ["商品名稱", "價格"]
        x.add_row([r1["prods"][i]["name"], r1["prods"][i]["price"]])
        x.align["商品名稱"] = "l"
        x.align["價格"] = "l"

    print(x)
    
    a = a
    page = int(input("前往頁碼："))


