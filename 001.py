import cv2

import numpy

a = numpy.ones([100,256,3])*255

for y in range(0,100):
    for x in range(0,256):
        a[y,x]= x


cv2.imshow("prprpr",a)

r,img = cv2.threshold(a,127,90,cv2.THRESH_BINARY)


cv2.imshow("prpr",img)

cv2.waitKey()





#cv2.putText(a,"prpr",(200,200),cv2.FONT_ITALIC,3,(0,120,34),8,8,False)
#cv2.line(a,(50,250),(500,250),(0,255,100),6)
#cv2.putText(a,"prpr",(200,300),cv2.FONT_ITALIC,3,(0,120,34),8,8,True)


                                 #a[0:799,0:799] = [123,245,0]

#cv2.line(a,(0,0),(700,700),(255,255,0),6)
#cv2.rectangle(a,(0,0),(300,200),(255,255,0),60)
#cv2.circle(a,(300,300),78,(255,255,0),80)