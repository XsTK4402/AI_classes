import cv2
import numpy as np
import IPython.display as dp

vc = cv2.VideoCapture("data/h3.mp4") #開啟檔案

while open:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        frame2 = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([80,60,0])
        upper_blue = np.array([140,255,190])
        mask = cv2.inRange(frame, lower_blue, upper_blue)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # binary, contours
        for i in range(len(contours)):
            cv2.drawContours(frame , contours, -1, (255,255,255), 2)
        
            area = cv2.contourArea(contours[i])
            if area > 5000:
                x, y, w, h = cv2.boundingRect(contours[i])
                cv2.rectangle(frame2, (x,y), (x+w,y+h), (0,0,255), 2)

        cv2.imshow("result", frame2)
        if cv2.waitKey(30) & 0xFF == 27:
            break
        
vc.release()
cv2.destroyAllWindows
