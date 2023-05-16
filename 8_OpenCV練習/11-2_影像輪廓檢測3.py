import cv2
import numpy as np

img1 = cv2.imread("data/logos.jpg", 0)
img2 = img1.copy()
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
imgtest = cv2.inRange(img2, (180), (255))

img1 = cv2.erode(img1, np.ones((30,30)))
img1 = cv2.dilate(img1, np.ones((15,15)))

img3  = np.full((img1.shape[0], img1.shape[1], 3), 255, np.uint8)


#劃出邊界矩形
binary, contours = cv2.findContours(img1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for i in range(len(binary)):
    cv2.drawContours(img3 , binary, -1, (255,255,255), 2)
    x, y, w, h = cv2.boundingRect(binary[i])
    cv2.rectangle(img2, (x,y), (x+w,y+h), (0,0,255), 2)

cv2.imshow("img1", img2)
cv2.waitKey(0)  