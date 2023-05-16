import cv2
import numpy as np
import IPython.display as dp

img1 = np.full((500, 500, 3), (150, 200, 16), np.uint8)
#            長、寬、圖像通道數   B   G    R
#         (1灰階、3彩色、 4透明度)                   

img2 = img1.copy() #備份

B, G, R = cv2.split(img2)  #將BGR拆開
img3 =  cv2.merge((B,G,R))

#直線
cv2.line(img1, (0,0), (500,500), (255, 0, 0), 2)
#cv2.line(圖像變數, 線的起點, 線的終點, 顏色, 線粗細)

#矩形
cv2.rectangle(img1, (300,400), (400,500), (255, 0, 0), -1)
#cv2.rectangle(圖像變數, 矩形左上點, 矩形右下點, 顏色, 線粗細)

#圓形
cv2.circle(img1, (100,300), 70, (255, 0, 0), 3)
#cv2.circle(圖像變數, 中心點, 半徑, 顏色, 線粗細(「-1」則實心圖形))



cv2.imshow('image', img3) 
cv2.waitKey(0)            