import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
x = pd.DataFrame(iris["data"], columns=iris["feature_names"])
# print(x)


import numpy as np
x_np = np.array(x)

from sklearn.cluster import KMeans
cluster = KMeans(n_clusters=3)
cluster.fit(x_np)
# print(cluster.cluster_centers_)
cluster.labels_

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from sklearn.metrics import silhouette_score
for i in range(2, 20):
    test = KMeans(n_clusters=i)
    test.fit(x_np)
    score = silhouette_score(x_np, test.labels_)
    print(i, ":", score)
    
import matplotlib.pyplot as plt
import seaborn as sns

xaxis = x["sepal length (cm)"]
yaxis = x["petal length (cm)"]
sns.scatterplot(x=xaxis, y=yaxis, hue=iris["target"])
plt.show()