import cv2
import numpy as np
import IPython.display as dp
from PIL import ImageFont, ImageDraw, Image
import time

for x in range (0,250,10):
    dp.clear_output(True) #等待新輸出True、False
    img1 = np.full((500, 500, 3), (100, 150, 50), np.uint8) #建立圖像
    img1 = Image.fromarray(img1) #將openCV格式轉換成ImageDraw格式
    
    ImageDraw.Draw(img1).text(
    (x,250), 
    "It is Never Correct", 
    (0, 0, 125), 
    ImageFont.truetype("C:/Windows/Fonts/times.ttf", 25)
)   #ImageDraw.Draw(PIL圖像變數).text(文字位置, 要寫的文字, 顏色, 設定)
    
    img1 = np.array(img1) #將ImageDraw格式轉換成openCV格式
    
    cv2.imshow('image', img1) 
    cv2.waitKey(100) 
    
    