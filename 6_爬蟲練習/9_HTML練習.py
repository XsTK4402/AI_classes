from bs4 import BeautifulSoup
import requests
import json
import codecs

r1 = requests.get("http://www.mol.gov.tw/1607/1632/1633/lpsimplelist", params={
    "Page": "1",
    "PageSize": "20"
})
b1 = BeautifulSoup(r1.text, "html.parser")
b2 = b1.find_all("h3")

for i in range(0, len(b2), 1):
    print(b2[i].find("a").attrs["title"])
    # print(b2[i].find("a").text, end=" ")
    # print(b2[i].parent.find("div",{"class": "data"}). find_all("span")[1].text)
    # print("=========================================================")

r2 = requests.get("http://www.mol.gov.tw"+b2[i].find("a").attrs["href"])
b3 = BeautifulSoup(r2.text, "html.parser")
# print(b3.find_all("body")[1].text)

with codecs.open("內容.txt", "a", "utf-8") as f:
    f.write(b2[i].parent.find("div", {"class": "data"}). find_all(
        "span")[1].text + "\r\n")
    f.write(b2[i].find("a").text + "\r\n")
    f.write("=========================================================\r\n")
    f.write(b3.find_all("body")[1].text)
    f.write("=========================================================\r\n\r\n")

# b3 = b1.find_all("div", {"class": "data"})
# for i in range(0, len(b3), 1):
#     print(b3[i]. find_all("span")[1].text)
