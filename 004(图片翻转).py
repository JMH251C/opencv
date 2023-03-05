import cv2
import numpy

img = cv2.imread("/home/jmh/图片/00rrrdt1.png",)

img2 = cv2.resize(img,None,fx=1.5,fy=1.5)

center = (len(img2[0])/2,len(img2)/2)

M = cv2.getRotationMatrix2D(center,90,1)

img3 = cv2.warpAffine(img2,M,(len(img2[0]),len(img2)))


cv2.imshow("prpr", img3)
cv2.waitKey()


#cv2.warpAffine(src,M,dsize,flags.borderMode,borderValue)
#src原始图像   M矩阵（变换像素位置） desize输出图片尺寸 borderMode可选  value可选参数

#center旋转中心坐标（XY元组）  angle角度  scale缩放比例1原比例

