import pytesseract as pt
import cv2
import numpy as np

img1 = cv2.imread("data/h2.png")
img2 = cv2.inRange(img1, (0,0,200), (0,0,255))

text = pt.image_to_string(img2, "chi_tra")
print("辨識結果：", text)


cv2.imshow("img", img2)
cv2.waitKey(0)
