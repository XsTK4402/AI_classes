from bs4 import BeautifulSoup
import requests
import json
import codecs

r1 = requests.get("https://udn.com/api/more",params = {
    "page" : "22",
    "id":"",
    "channelId":"1",
    "cate_id":"0",
    "type":"breaknews",
    "totalRecNo":"26304"
})

d = json.loads(r1.text)

for i in range(0, len(d["lists"]), 1):

    print(d["lists"][i]["time"]["date"], d["lists"][i]["title"])

    r2 = requests.get("https://udn.com"+d["lists"][i]["titleLink"])

    if r2.status_code == 200:

        bl = BeautifulSoup(r2.text, "html.parser")

        with codecs.open("udn.txt", "a", "utf-8") as f:

            f.write(d["lists"][i]["time"]["date"]+"\r\n")

            f.write(d["lists"][i]["title"]+"\r\n")

            section = bl.find("section", {"class": "article-content__editor"})

            if section != None:

                for data in section.find_all("p"):

                    f. write(data.text)

                    f.write(
                        "=========================================================\r\n\r\n")
