from keras.datasets import mnist
import tensorflow 
# ((x_train, y_train), (x_test, y_test))
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# print(x_train)

import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame(x_train[0])

# fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(15,3))

# for i in range(5):
#     ax[i].imshow(x_train[i])
#     ax[i].set_title('Label: {}'.format(y_train[i]))

plt.imshow(x_train[2])
plt.show() 
# print(df)

from keras.models import Sequential
from keras.layers import Dense

layers = [
    Dense(128, activation="sigmoid", input_dim=784),
    Dense(10, activation="sigmoid")
]

model = Sequential(layers)
model.summary()

model.compile(loss="mse", metrics="accuracy")

from keras.utils import to_categorical

y_train_cat = to_categorical(y_train, num_classes=10)
y_teest_cat = to_categorical(y_test, num_classes=10)

print(y_train[0])
print(y_train_cat[0])

