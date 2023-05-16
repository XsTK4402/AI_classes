import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.metrics import confusion_matrix
import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
import seaborn as sns

img_height = 224 
img_width = 224
batch_size = 32 # 像素在大的話就不適合繼續用太低  
LR = 0.01  # 加0補0測試 adam預設為0.001
EPOCHS = 30

model = load_model("C:\\Users\\Matthew\\Desktop\\測試用h5檔案\\keras_model.h5")

# # ----------3classes 用的----------
classes = []
start = 2457
end = 2459
for c in range(start, end+1):
    classes.append(f"Endgame_{c}")
    
print(len(classes))
print(classes)

def prepare_image(file):
    img = image.load_img(file, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

#@title # 預測 圖片在同一資料夾
meme_path = "C:\\Users\\Matthew\\Desktop\\新增資料夾\\"
file_extensions = ["jpg", "jpeg", "png"]
pres = []
ans = []
for f in os.listdir(meme_path):
    if f.split(".")[-1].lower() in file_extensions:
        image_name = os.path.join(meme_path, f)
        preprocessed_image = prepare_image(image_name)
        predictions = model.predict(preprocessed_image)
        index = np.argmax(predictions)
        print("image：", f)
        print("class：", classes[index])
        f = f.split("_")
        ans.append(f"{f[0]}_{f[1]}")
        pres.append(classes[index])
        
# 混淆矩陣
cm = confusion_matrix(ans, pres)
df = pd.DataFrame(cm, columns=classes, index=classes)
plt.figure(figsize=(13, 13)) # cell要設置在欲呈現的圖案上
# plt.figure(figsize=(5, 5))
sns.heatmap(cm,
      annot=True,
      fmt="d",
      cmap="Blues",
      xticklabels=classes,
      yticklabels=classes
)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
        
        