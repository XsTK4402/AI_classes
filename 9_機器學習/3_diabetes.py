from sklearn.tree import DecisionTreeRegressor  # 回歸問題
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import requests
import numpy as np
import io

r1 = requests.get(
    "https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt")
data = r1.content.decode('utf-8')
data = pd.read_csv(io.StringIO(data), sep='\t')
# print(data)

x = data.drop("Y", axis=1)
y = data["Y"]
x_np = np.array(x)
y_np = np.array(y)
x_train, x_test, y_train, y_test = train_test_split(x_np, y_np, test_size=0.1)
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

reg = DecisionTreeRegressor(max_depth = 3)
reg.fit(x_train, y_train)

plt.figure(figsize=(14, 14))
plot_tree(reg, 
     feature_names=x.columns, 
     filled=True)
# plt.show()

pre = reg.predict(x_test)
print(r2_score(y_test, pre))