import cv2, numpy

img1 = cv2.imread("data/1.jpg", 1)
# print(img1.shape[0],img1.shape[1],img1.shape[2])

Bavg=img1[:,:,0].mean()
Gavg=img1[:,:,1].mean()
Ravg=img1[:,:,2].mean()

img2 = img1.copy()

img2[:,:,0]=cv2.multiply(img1[:,:,0], ((Ravg+Gavg+Bavg)/(Bavg*3)))
img2[:,:,1]=cv2.multiply(img1[:,:,1], ((Ravg+Gavg+Bavg)/(Gavg*3)))
img2[:,:,2]=cv2.multiply(img1[:,:,2], ((Ravg+Gavg+Bavg)/(Ravg*3)))

# cv2.imshow('image', img1)
cv2.imshow('image', img2)
cv2.waitKey(0)   