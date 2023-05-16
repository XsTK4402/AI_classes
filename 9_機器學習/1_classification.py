from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

iris = load_iris()
x = pd.DataFrame(iris["data"], columns=iris["feature_names"])
y = iris["target"]

# total = x[:]
# total["ans"] = iris["target"]
# total.to_csv("data/iris.csv", index=False, encoding="utf-8")
# 先把資料分成兩份，一份訓練/一份驗證

# print(train_test_split([1, 2, 3,4], test_size = 1))

x_np = np.array(x)
y_np = np.array(y)
x_train, x_test, y_train, y_test = train_test_split(x_np, y_np, test_size=0.1)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
