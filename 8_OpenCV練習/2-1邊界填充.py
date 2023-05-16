import cv2
import numpy as np
import IPython.display as dp

img1 = cv2.imread("data/1.jpg", 1)
img1 = cv2.resize(img1, (0,0), fx = 0.5, fy = 0.5)

top_size, bottom_size, left_size, right_size = (50,50,50,50)

replicate = cv2.copyMakeBorder(img1, top_size, bottom_size, left_size, right_size, borderType=cv2. BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1, top_size,bottom_size, left_size, right_size,cv2. BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
wrap = cv2. copyMakeBorder(img1, top_size, bottom_size, left_size, right_size, cv2. BORDER_WRAP)
constant = cv2. copyMakeBorder(img1, top_size, bottom_size, left_size, right_size, cv2. BORDER_CONSTANT, value=0)



cv2.imshow('replicate', replicate) 
cv2.imshow('reflect', reflect) 
cv2.imshow('reflect101', reflect101) 
cv2.imshow('wrap', wrap) 
cv2.imshow('constant', constant) 

cv2.waitKey(0)            