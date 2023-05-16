import cv2
import numpy as np

img1 = cv2.imread("qrcode.jpg")
img1 = cv2.resize(img1, (0,0), fx = 0.5, fy = 0.5)

img3 = cv2.blur(img1, (2, 1))  #平均值模糊法(統計範圍內的色彩值平均)
img4 = cv2.medianBlur(img1, 5)  #中值模糊法(將處理範圍內的色彩值做排序，取順序在中間的)
img45 = cv2.GaussianBlur(img1, (3, 3), 0)  #高斯模糊

img2 = cv2.Canny(img1, 800 , 1000) #邊緣偵測

#影像銳利化 - 僅灰階，須將BGR分開做
img5 = img1.copy()
img5[:,:,0] = cv2.equalizeHist(img1[:,:,0])
img5[:,:,1] = cv2.equalizeHist(img1[:,:,1])
img5[:,:,2] = cv2.equalizeHist(img1[:,:,2])

res = np.hstack((img1, img4, img45))
cv2.imshow("result", res)
cv2.imshow('image', img2) 
cv2.waitKey(0)   