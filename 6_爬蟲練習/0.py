import requests

url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E8%A1%80%E5%A3%93%E8%A8%88&page=1&sort=sale/dc"

res = requests.get(url.format(1))

res_json = res.json()

total_page = res.json()["totalPage"]

for i in range(1, total_page + 1)[:10]:
  try:
    print(f"爬取第{i}資料中")
    target_url = url.format(i)

    res = requests.get(target_url)
    res_json = res.json()

    for prod in res_json["prods"]:
      print(prod["name"])
      with open("file.txt", "w") as f:
        f.write(prod["name"] + "\n")
  except:
    print(f"第{i}出現問題。")