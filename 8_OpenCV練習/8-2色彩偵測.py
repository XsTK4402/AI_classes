import cv2
import numpy as np
import IPython.display as dp
from PIL import ImageFont, ImageDraw, Image

def empty(v):
    pass

img1 = cv2.imread("data/bluepen.jpg", 1)
img1 = cv2.resize(img1, (0,0), fx = 0.4, fy = 0.4)

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar',640, 320)

cv2.createTrackbar("Hue Min", "trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Val Max", "trackbar", 255, 255, empty)

while True:
    h_min = cv2.getTrackbarPos("Hue Min", 'trackbar')
    h_max = cv2.getTrackbarPos("Hue Max", 'trackbar')
    s_min = cv2.getTrackbarPos("Sat Min", 'trackbar')
    s_max = cv2.getTrackbarPos("Sat Max", 'trackbar')
    v_min = cv2.getTrackbarPos("Val Min", 'trackbar')
    v_max = cv2.getTrackbarPos("Val Max", 'trackbar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper)
    
    result = cv2.bitwise_and(img1, img1, mask=mask)
    
    cv2.imshow("img1", img1)
    cv2.imshow("hsv", hsv)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    if cv2.waitKey(10) & 0xFF == 27:
            break

