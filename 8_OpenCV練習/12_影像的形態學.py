import cv2
import numpy as np

img1 = cv2.imread("data/hair.jpg", 1)
img1 = 255 - img1
img1 = cv2.resize(img1, (0,0), fx = 1.2, fy = 1.2)

#線條侵蝕(色彩值低的會侵蝕色彩值高的)：
#結果圖像=cv2.erode(圖像變數, 結構陣列)
img2 = cv2.erode(img1, np.ones((10, 10)), iterations= 2)
#            結構陣列 -->np.ones(範圍大小)
img3 = cv2.dilate(img2, np.ones((10,10)), iterations= 2)
#線條膨脹(色彩值高的會侵蝕色彩值低的)↑

#先腐蝕，再膨脹
img4 = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, np.ones((5,5)))
# cv2.MORPH_ERODE	圖像的侵蝕操作
# cv2.MORPH_DILATE	圖像的膨脹操作
# cv2.MORPH_OPEN	先進行圖像的膨脹操作，再進行侵蝕操作
# cv2.MORPH_CLOSE	先進行圖像的侵蝕操作，再進行膨脹操作
# cv2.MORPH_GRADIENT	計算圖像的形態學梯度
# cv2.MORPH_TOPHAT	計算圖像的頂帽運算
# cv2.MORPH_BLACKHAT	計算圖像的黑帽運算
  
res = np.hstack((img1, img2, img3))
cv2.imshow('img4', img4) 
cv2.waitKey(0)    