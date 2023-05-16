import cv2
import numpy as np
import IPython.display as dp
from PIL import ImageDraw, Image

x = 0
y = True
while y == True:
    if x <= 400 :
        dp.clear_output(True) 
        img1 = np.full((500, 500, 3), (0, 0, 255), np.uint8) 
        img1 = Image.fromarray(img1)
        
        ImageDraw.Draw(img1).rectangle(
        ((x,200),(x+100,300)), 
        fill="black")  
        
        img1 = np.array(img1) 
        
        cv2.imshow('image', img1) 
        key = cv2.waitKey(50)
        if key != -1: 
            break
        
        x = x+10
        if x == 400:
            y = False

        while y == False:
            dp.clear_output(True) 
            img1 = np.full((500, 500, 3), (0, 0, 255), np.uint8)
            img1 = Image.fromarray(img1)
            
            ImageDraw.Draw(img1).rectangle(
            ((x,200),(x+100,300)), 
            fill="black")  
            
            img1 = np.array(img1) 
            
            cv2.imshow('image', img1) 
            key = cv2.waitKey(50)
            if key != -1: 
                break
            
            x = x-10
            if x == 0:
                y = True
