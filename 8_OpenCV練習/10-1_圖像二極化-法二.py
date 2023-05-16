import cv2
import numpy as np

img1 = cv2.imread("data/1.jpg", 1)


img2 = img1.copy()
img2[:,:,0] = cv2.adaptiveThreshold(img1[:,:,0], 100, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 151, 0)
img2[:,:,1] = cv2.adaptiveThreshold(img1[:,:,1], 100, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 151, 0)
img2[:,:,2] = cv2.adaptiveThreshold(img1[:,:,2], 100, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 151, 0)

cv2.imshow('image', img2) 
cv2.waitKey(0)   