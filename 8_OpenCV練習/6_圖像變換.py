import cv2, numpy

img1 = cv2.imread("data/1.jpg", 1)

width = 500

#圖像縮放                #tuple(長,寬)
img2 = cv2.resize(img1, (int(width * (1612/1016)), width))

#圖像翻轉
img3 = cv2.flip(img1, 1)
# 1 => 左右翻轉
# 0 => 上下翻轉
# -1 => 左右與上下皆翻轉

#圖像旋轉
img4 = cv2.warpAffine(img1, cv2.getRotationMatrix2D((50,50), 45, 0.1), (int(width * (1612/1016)), width))
#結果圖像=
#cv2.warpAffine(圖像變數, cv2.getRotationMatrix2D(旋轉中心, 角度, 縮放比率), 輸出的圖像大小)

cv2.imshow('image', img6) 
cv2.waitKey(0)   