# from urllib.request import urlretrieve

# url = "https://raw.githubusercontent.com/Elwing-Chou/tibaml0315/main/train.csv"
# urlretrieve(url, "data/titanic_train.csv")

# url2 = "https://raw.githubusercontent.com/Elwing-Chou/tibaml0315/main/test.csv"
# urlretrieve(url, "data/titanic_test.csv")

import pandas as pd
train = pd.read_csv("data/titanic_train.csv", encoding="utf-8")
test = pd.read_csv("data/titanic_test.csv", encoding="utf-8")

total = pd.concat([train, test], axis = 0)
total = total.drop(["PassengerId", "Survived"], axis = 1)
# print(total)

def cabin(c):
    if pd.isna(c):
        return c
    else:
        return c[0]
total["Cabin"] = total["Cabin"].apply(cabin)

c = total["Ticket"].value_counts()
def ticket(t):
    if pd.isna(t):
        return t
    else:
        return c[t]
total["Ticket"] = total["Ticket"].apply(ticket)


import re
# 平常
# n = "Braund, Mr. Owen Harris"
# n.split(".")[0].split(",")[-1]
def name(n):
    if pd.isna(n):
        return n
    else:
        pat = r".+,(.+?)\..+"  
        mid = re.match(pat, n).group(1)
        return mid.strip()
total["Name"] = total["Name"].apply(name)

s = total.isna().sum()
s[s != 0].sort_values(ascending=False)

med = total.median().drop("Pclass")
total = total.fillna(med)

print(total)