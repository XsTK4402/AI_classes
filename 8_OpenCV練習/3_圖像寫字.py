import cv2
import numpy as np
import IPython.display as dp
from PIL import ImageFont, ImageDraw, Image

img1 = cv2.imread("data/1.jpg", 1)

img2 = img1.copy() #備份

wimg1 = Image.fromarray(img1) #將openCV格式轉換成ImageDraw格式

ImageDraw.Draw(wimg1).text(
    (0,0), 
    "It is Never Correct", 
    (0, 0, 125), 
    ImageFont.truetype("C:/Windows/Fonts/times.ttf", 999)
)
#ImageDraw.Draw(PIL圖像變數).text(文字位置, 要寫的文字, 顏色, 設定)

new_img1 = np.array(wimg1) #將ImageDraw格式轉換成openCV格式


cv2.imshow('image', new_img1) 
cv2.waitKey(0)            