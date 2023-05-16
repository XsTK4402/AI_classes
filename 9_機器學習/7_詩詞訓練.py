from urllib.request import urlretrieve
# url = "https://raw.githubusercontent.com/Elwing-Chou/tibaml0315/main/poem_test.txt" 
# urlretrieve(url, "data\poem_test.csv")

# url = "https://raw.githubusercontent.com/Elwing-Chou/tibaml0315/main/poem_train.txt" 
# urlretrieve(url, "data\poem_train.csv")
#下載所需檔案

import pandas as pd
train = pd.read_csv("data/poem_train.csv", encoding="utf-8")
test = pd.read_csv("data/poem_test.csv", encoding="utf-8")

poets = train["作者"].value_counts().index
# print(poets) #找出詩中的所有作者

p2idx = {p:i for i, p in enumerate(poets)}
# print(p2idx)

y_train = train["作者"].replace(p2idx)
y_test = test["作者"].replace(p2idx)
# print(y_test)

import os
import jieba
if not os.path.exists("data\dict.txt.big"):
    url = "https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big"
    urlretrieve(url, "dict.txt.big")
# 古詩你載入大詞典, 反而有可能有錯, 我已經試過了, 讓他猜比較準
# jieba.set_dictionary("dict.txt.big")
# 有in(要轉換的), 有out(轉換成的東西)
def trans(s):
    return " ".join(jieba.cut(s))
x_train = train["內容"].apply(trans)
x_test = test["內容"].apply(trans)
# print(x_test)

from sklearn.feature_extraction.text import CountVectorizer
vec = CountVectorizer()
x_train_vec = vec.fit_transform(x_train)
x_test_vec = vec.transform(x_test)
print(x_train_vec)

import numpy as np
y_train = np.array(y_train)
y_test = np.array(y_test)

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB(alpha=0.25)
clf.fit(x_train_vec, y_train)

from sklearn.metrics import accuracy_score
pre = clf.predict(x_test_vec)
print(accuracy_score(y_test, pre))  #0.86666666666666667