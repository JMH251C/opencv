
import cv2

capture = cv2.VideoCapture(0) #调用摄像头，内置为0,其他依次增加

retval,image = capture.read() #摄像头读取返回值

while 1:
    ret,img = capture.read()
    img2 = cv2.resize(img, None, fx=1.5, fy=1.5) #翻转画面

    center = (len(img2[0]) / 2, len(img2) / 2)

    M = cv2.getRotationMatrix2D(center, -45, 1)

    img3 = cv2.warpAffine(img2, M, (len(img2[0]), len(img2)))
    imgk = cv2.flip(img,1)

    cv2.imshow("img",img3)
    cv2.imshow("2",imgk)
    k = cv2.waitKey(1)
    if k == 27:
        break


capture.realease()  #清除摄像头缓存（可不写）

































