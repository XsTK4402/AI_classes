import cv2
import os
from skimage.metrics import structural_similarity as ssim
# 直接使用skimage內建的計算模組

imagelist = os.listdir('clip/')
imagelist = sorted(imagelist, key=lambda x: os.path.getmtime(os.path.join('clip', x)))
# 讀取資料夾下所有文件的名字並排序
# print(imagelist)

path = 'clip/ssim.txt'
f = open(path, 'w')
# 以寫入模式開啟紀錄用txt檔案(用來記錄相似度過低的偵數)

for i in range(len(imagelist)-1)[::3]:
# 每三偵去跑imagelist裡頭的圖片(為加快速度)
# for i in range(396,430)[::5]:
    a = imagelist[i]
    b = imagelist[i+2]

    img1 = cv2.imread(f"clip/{a}")
    img2 = cv2.imread(f"clip/{b}")
    # 用opencv讀取i 跟i+2 的圖片檔案

    # gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    # gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # 轉為灰階圖片

    # ssim_val = ssim(gray_img1, gray_img2)
    ssim_val = ssim(img1, img2, channel_axis=2)
    # 計算SSIM值

    if ssim_val < 0.6:
        f.write(f"{a} and {b} ssim : {ssim_val}\n")
    # 輸出SSIM值，並將低於指定值者寫入txt檔

f.close()
