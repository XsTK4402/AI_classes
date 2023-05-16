import cv2

img1 = cv2.imread("data/shapes.jpg", 1)
cv2.imshow('origin', img1) 
img2 = img1.copy()
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img1, 150, 200)
countours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


for cnt in countours:
    cv2.drawContours(img2 , cnt, -1, (255,255,255), 2)
    # print(cv2.contourArea(cnt)) #輪廓面積
    peri = cv2.arcLength(cnt, True) #輪廓邊長(True為閉合圖形、 False為開放圖形)
    vertices = cv2.approxPolyDP(cnt, peri*0.025, True)  
    #輪廓邊長(True為閉合圖形、 False為開放圖形)
    corners = len(vertices)
    x, y, w, h = cv2.boundingRect(vertices)
    cv2.rectangle(img2, (x,y), (x+w,y+h), (0,0,255), 3)
    if corners == 3:
        cv2.putText(img2, "triangel", (x, y-7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    if corners == 5:
        cv2.putText(img2, "pentagon", (x, y-7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    if corners == 6:
        cv2.putText(img2, "6_angle", (x, y-7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    if corners == 7:
        cv2.putText(img2, "7_angle", (x, y-7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    if corners == 8:
        cv2.putText(img2, "8_angle", (x, y-7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    if corners == 9:
        cv2.putText(img2, "almost_circle", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)


cv2.imshow("detected", img2)
cv2.waitKey(0)  