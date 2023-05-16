from sklearn.tree import DecisionTreeClassifier, plot_tree #分類問題
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()
x = pd.DataFrame(iris["data"], columns=iris["feature_names"])
y = iris["target"]

x_np = np.array(x)
y_np = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x_np, y_np, test_size=0.1)

clf = DecisionTreeClassifier(max_depth=2)
a = clf.fit(x_train, y_train)
# print(plot_tree(a))
plt.figure(figsize=(14,14))
plot_tree(clf, 
    feature_names=x.columns, 
    class_names=iris["target_names"],
    filled=True)

# plt.show()
pre = clf.predict(x_test)
print(accuracy_score(y_test, pre))
