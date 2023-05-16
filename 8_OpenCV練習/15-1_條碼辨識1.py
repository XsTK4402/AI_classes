from pyzbar import pyzbar
import cv2
import numpy as np

img1 = cv2.imread("data/qrcode1.jpg")
qrcode = pyzbar.decode(img1)

for d in qrcode:
    print("條碼類型：", d.type)
    try:
        print("資料：", d.data.decode("utf-8").encode("sjis").decode("utf-8"))
    except:
        print("資料：", d.data.decode("utf-8"))
    x, y, w, h = d.rect
    cv2.rectangle(img1, (x,y), (x+w, y+h), (0,0,0), 2)
    print("==================================================")

cv2.imshow("img", img1)
cv2.waitKey(0)