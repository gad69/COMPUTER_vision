import cv2
img = cv2.imread('u.png')
scale_percent = 2
width = int(img.shape[1]*scale_percent)
height = int(img.shape[0]*scale_percent)
dim = (width,height)
resized = cv2.resize(img,dim,interpolation=cv2.INTER_CUBIC )
cv2.imwrite('resised.jpg',resized)