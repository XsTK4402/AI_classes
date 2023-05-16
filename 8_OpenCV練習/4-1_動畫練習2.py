import cv2
import numpy as np
import IPython.display as dp
from PIL import ImageFont, ImageDraw, Image
import time

v1 = cv2.VideoWriter("C:/Users/Matthew/Desktop/python/data/1.mp4", 
                     cv2.VideoWriter_fourcc(*"MP4V"), 
                     30, 
                     (500,500)
)

for x in range (0,250,10):
    
    img1 = np.full((500, 500, 3), (100, 150, 50), np.uint8) #建立圖像
    img1 = Image.fromarray(img1) #將openCV格式轉換成ImageDraw格式
    
    ImageDraw.Draw(img1).text(
    (x,250), 
    "It is Never Correct", 
    (0, 0, 125), 
    ImageFont.truetype("C:/Windows/Fonts/times.ttf", 25)
)   #ImageDraw.Draw(PIL圖像變數).text(文字位置, 要寫的文字, 顏色, 設定)
    
    img1 = np.array(img1) #將ImageDraw格式轉換成openCV格式
    
    v1.write(img1)
    time.sleep(1)
    
v1.release()
    