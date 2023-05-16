import cv2
import numpy as np

#圖像轉灰階，二極化(黑白)，找邊緣


img1 = cv2.imread("data/hair.jpg", 0)
img1 = cv2.resize(img1, (0,0), fx = 1.5, fy = 1.5)
img2 = np.full((img1.shape[0], img1.shape[1], 3), 255, np.uint8)

# th, img3 = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)
img4 = cv2.inRange(img1, (180), (255))
# img_canny = cv2.Canny(img1, 200, 250)

binary, contours = cv2.findContours(img4, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img2, binary, -1, (0,0,0), 2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)  