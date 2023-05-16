import cv2
import numpy as np

#閾值處理
# ret, dst = cv2.threshold(src, thresh, maxval, type))
# src:输入图,只能输入单通道图像,通常来说为灰度图
# dst:輸出圖像
# thresh:閥值
# maxval:當像素值超過閥值(或小於閥值，取決於type)，所賦的值
# type:
# cv2.THRESH_BINARY	大於閾值的像素設為最大值，小於閾值的像素設為0
# cv2.THRESH_BINARY_INV	cv2.THRESH_BINARY 的反轉
# cv2.THRESH_TRUNC	大於閾值的像素設為閾值，小於等於閾值的像素不變
# cv2.THRESH_TOZERO	大於閾值的像素不變，小於等於閾值的像素設為0
# cv2.THRESH_TOZERO_INV	cv2.THRESH_TOZERO 的反轉
# cv2.THRESH_MASK	使用位元運算的閾值處理方法
# cv2.THRESH_OTSU	基於大津方法的自適應閾值處理方法
# cv2.THRESH_TRIANGLE	基於三角形閾值法的自適應閾值處理方法


img1 = cv2.imread("data/1.jpg", 0)
img2 = img1.copy()
th, img2 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(th)
# th, img2[:,:,1] = cv2.threshold(img1[:,:,1], 127,255, cv2.THRESH_BINARY)
# print(th)
# th, img2[:,:,2] = cv2.threshold(img1[:,:,2], 127,255, cv2.THRESH_BINARY)
# print(th)



# img2 = img1.copy()
# th, img2[:,:,0] = cv2.threshold(img1[:,:,0], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, img2[:,:,1] = cv2.threshold(img1[:,:,1], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, img2[:,:,2] = cv2.threshold(img1[:,:,2], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)

cv2.imshow('img1', img1) 
cv2.imshow('img2', img2) 
cv2.waitKey(0)   