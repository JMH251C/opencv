import cv2
import numpy
a = cv2.imread("/home/jmh/图片/00rrrdt1.png",0)

for y in range(0,100):
    for x in range(0,256):
        a[y, x] = x

cv2.imshow("prprpr", a)

r, img = cv2.threshold(a, 127, 255, cv2.THRESH_BINARY_INV)                #阈值化处理    ——INV反处理   src:对象
t,img2 = cv2.threshold(a, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("prpr", img)
cv2.imshow("pr1pr", img2)
cv2.waitKey()







