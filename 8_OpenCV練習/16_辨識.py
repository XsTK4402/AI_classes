from pyzbar import pyzbar
import cv2
import numpy as np

img1 = cv2.imread("data/pic.jpg")
img1 = cv2.resize(img1, (0,0), fx=0.3, fy=0.3)

classifier = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

ret = classifier.detectMultiScale(img1, minNeighbors=10, minSize=(5,5))

for x, y, w, h in ret:
    cv2.rectangle(img1, (x,y), (x+w, y+h), (0,0,0), 2)
    print("==================================================")

cv2.imshow("img", img1)
cv2.waitKey(0)