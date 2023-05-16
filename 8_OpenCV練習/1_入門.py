import cv2
import numpy as np
import IPython.display as dp

img1 = cv2.imread("data/1.jpg", 1) #1一般(不含透明度) 、 -1完整(包含透明度) 、 0灰階
img1 = cv2.resize(img1, (0,0), fx = 0.5, fy = 0.5) #調整0.5倍大

# print(img1)

img1.shape[0] #取得圖片高
img1.shape[1] #取得圖片寬
img1.shape[2] #取得當前色彩空間的通道數量
# print(img1.shape)


img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
                        # cv2.COLOR_BGR2HSV
                        # cv2.COLOR_BGR2GRAY
                        # cv2.COLOR_HSV2BGR
                        # cv2.COLOR_GRAY2BGR
# print(img2)

# cv2.imwrite("data/1.1.png", img1, [cv2.IMWRITE_PNG_COMPRESSION, 9]) #儲存圖片

# cv2.IMWRITE_JPEG_QUALITY：JPEG品質，0-100，值越高越好。
# cv2.IMWRITE_PNG_COMPRESSION：PNG壓縮級別，0-9，值越高壓縮率越高，文件大小越小。
# cv2.IMWRITE_WEBP_QUALITY：WebP品質，1-100，值越高越好。


cv2.imshow('image', img1) #顯示圖像("圖像的視窗名稱", "要顯示的圖像資料")
cv2.waitKey(0)            #暫停程序的執行，直到用戶按下一個按鍵。(不設定會閃退)