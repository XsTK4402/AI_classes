import cv2
import numpy as np

img1 = cv2.imread("data/h2.png")  # 紅字為 0,0,255


img2 = cv2.subtract(img1, (255,255,254,0))
img3 = img2 * 255
img4 = img3[:,:,2]
img5 = cv2.bitwise_not(img4)

cv2.imshow('image', img5)
cv2.waitKey(0)
cv2.destroyAllWindows()
