import cv2, numpy

img1 = cv2.imread("data/1.jpg", 1)

#相加 - 變亮(大於255的會直接等於255)：
img2 = cv2.add(img1, img1)

#純色相加
img20 = numpy.full(img1.shape, 20, numpy.uint8)
img4 = cv2.add(img1, img20)
#---------------------------------------------------------#
#相減 - 負片效果
img255 = numpy.full(img1.shape, 255, numpy.uint8)
img_negative = cv2.subtract(img255, img1)

#相減 - 變暗(大於255的會直接等於255)：
img5 = cv2.subtract(img1, img1) #自己減自己為(0,0,0)全黑

#純色相減
img20 = numpy.full(img1.shape, 20, numpy.uint8)
img7 = cv2.subtract(img1, img20)
#---------------------------------------------------------#
#圖像相除(未整除的會四捨五入)
#很快地變暗
img10 = numpy.full(img1.shape, 10, numpy.uint8)
img8 = cv2.divide(img1, img10)

#圖像相乘(大於255的會直接等於255)
#很快地變暗
img9 = cv2.multiply(img1, img10)



cv2.imshow('image', img9) 
cv2.waitKey(0)   