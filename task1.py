import cv2
import numpy as np

imcap = cv2.VideoCapture(0)
imcap.set(3, 640) # set width as 640
imcap.set(4, 480) # set height as 480
while True:
    _, frame = imcap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    l_g=np.array([36, 25, 25])
    u_g=np.array([70, 255,255])

    mask=cv2.inRange(hsv,l_g,u_g)

    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    key=cv2.waitKey(1)
    if key==27:
        break
cv2.destroyAllWindows()