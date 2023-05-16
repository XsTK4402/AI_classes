hsinchu = {
    "名稱": "新竹",
    "人口": 100000,
    "是不是首都": False,
}

taipei = {
    "名稱": "台北",
    "人口": 3000000,
    "是不是首都": True,
}

Taiwan = [hsinchu, taipei]

print(Taiwan[1]["名稱"])

tokyo = {
    "名稱": "東京",
    "人口": 500000,
    "是不是首都": True,
}

osaka = {
    "名稱": "大阪",
    "人口": 2000000,
    "是不是首都": False,
}

Japan = [tokyo, osaka]

earth = {
    "台灣": Taiwan,
    "日本": Japan,
}

print(earth["日本"][0]["名稱"])