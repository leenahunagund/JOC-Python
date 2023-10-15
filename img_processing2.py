#image enhancement CLAHE

import cv2 #opencv

#read the image
img=cv2.imread('img.jpeg')

#prep for clahe
clahe=cv2.createCLAHE()

#convert to grey scale img
gray_img=cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

#apply enhancement
enh_img=clahe.apply(gray_img)

#save it to a file
cv2.imwrite('enhanced.jpeg',enh_img)

print('done enhancing')
