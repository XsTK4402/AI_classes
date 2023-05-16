from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

r1 = requests.get("https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html", headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'},
    params={
    "ID": "Wed%20Mar%2008%202023%2020:48:46%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93"
})

b1 = BeautifulSoup(r1.text, "html.parser")

countries = []
degrees = []

for county in b1.find_all('th'):
    countries.append(county.text)

for degree in b1.find_all('span')[::2]:
    degrees.append(degree.text)
    

x = PrettyTable()

for i in range(0, len(countries), 1):
    x.field_names = ["地區", "氣溫"]
    x.add_row([countries[i], degrees[i]])

print(x)
