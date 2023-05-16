import cv2
import os
from keras.preprocessing.image import ImageDataGenerator

# datagen = ImageDataGenerator(
#     featurewise_center=False,               # 去中心值，使數據集均值為0
#     samplewise_center=False,                # 使每個輸入樣本除以自身標準差
#     featurewise_std_normalization=False,    # 去中心值，使輸入樣本均值為0
#     samplewise_std_normalization=False,     # 使每個輸入樣本除以自身標準差(只考慮自身圖片)
#     zca_whitening=False,                    # 一種PCA降維處理，減少圖片的冗餘信息，保留最重要的特徵
#     zca_epsilon=1e-6,                       # zca白話的值
#     rotation_range=0.,                      # 使圖片隨機旋轉的角度，輸入一個值，演算法會使圖片在這個值區間隨機旋轉
#     width_shift_range=0.,                   # 圖片水平平移的尺寸
#     height_shift_range=0.,                  # 圖片垂直平移的尺寸
#     shear_range=0.,                         # 隨機裁減的角度
#     zoom_range=0.,                          # 隨機縮放大小
#     channel_shift_range=0.,                 # 隨機改變圖片的顏色
#     fill_mode='nearest',                    # 圖片經處理後邊界以外的點的處理方式
#     cval=0.,                                  
#     horizontal_flip=False,                  # 隨機進行水平翻轉
#     vertical_flip=False,                    # 隨機進行垂直翻轉
#     rescale=None,                           # 對圖片的每個像素值乘上這個縮放值，可理解為圖片正規化
#     preprocessing_function=None,            # 其他的前處理功能，可自行寫def定義或是使用套件提供的
# )

# datagen = ImageDataGenerator(
#     zca_whitening=False,          # 一種PCA降維處理，減少圖片的冗餘信息，保留最重要的特徵
#     rotation_range=40,            # 使圖片隨機旋轉的角度，輸入一個值，演算法會使圖片在這個值區間隨機旋轉
#     width_shift_range=0.2,        # 圖片水平平移的尺寸
#     height_shift_range=0.2,       # 圖片垂直平移的尺寸
#     shear_range=0.2,              # 隨機裁減的角度
#     zoom_range=0.2,               # 隨機縮放大小
#     horizontal_flip=True,         # 隨機進行水平翻轉
#     fill_mode="nearest")          # 圖片經處理後邊界以外的點的處理方式

# datagen = ImageDataGenerator(shear_range = 10)
datagen = ImageDataGenerator(rotation_range = 8)
# datagen = ImageDataGenerator(channel_shift_range = 150)

for i in range(2457, 2461):
    file_path = f"C:\\Users\\Matthew\\Desktop\\halfhalf\\80080010100\\Endgame_{i}"
    # file_path = "C:\\Users\\Matthew\\Desktop\\python\\test"
    file = os.listdir(file_path)
    preview = f"C:\\Users\\Matthew\\Desktop\\halfhalf\\80080010100\\Endgame_{i}"
    # preview = "C:\\Users\\Matthew\\Desktop\\python\\test\\new"

    print(file_path)


    for pic in file:
        img = cv2.imread(os.path.join(file_path, pic))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.reshape((1,) + img.shape)

        for batch in datagen.flow(img, batch_size=1, save_to_dir=preview, save_prefix="new_", save_format="jpg"):
            break