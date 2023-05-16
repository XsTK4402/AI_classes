import cv2
import numpy

img1 = cv2.imread("data/1.jpg", 1)
img2 = cv2.imread("data/3.jpg", 1)
img2 = cv2.resize(img2, (1612,1016))
# print(img1.shape[0],img1.shape[1],img1.shape[2])

# 透過numpy的矩陣變數功能可以作到裁切效果：
img1[0: 1016, 0: 1612:2] = img2[0: 1016, 0: 1612:2]
# 圖像變數[Y軸範圍起始:Y軸範圍結束:間格距離, X軸範圍起始: X軸範圍結束:間格距離]

img3 = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)
#加權圖像整合


cv2.imshow('image', img3)
cv2.waitKey(0)
