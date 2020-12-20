import numpy as np
import cv2
from pyzbar.pyzbar import decode
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
with open('mydata.txt') as f:
    mydatalist=f.read().splitlines()
print(mydatalist)
while True:
    success, img=cap.read()
    for barcode in decode(img):
        print(barcode.data)
        mydata=barcode.data.decode('utf-8')
        print(mydata)
        if mydata in mydatalist:
            outp="Authorized"  
            mycolor=(0,255,0)
        else:
            outp="Un-authorized"
            mycolor=(0,0,255)
        pts=np.array([barcode.polygon], np.int32)
        pts=pts.reshape((-1,1,2))
        cv2.polylines(img, [pts], True, mycolor, 5)
        pts2=barcode.rect
        cv2.putText(img,outp,(pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, mycolor, 2)
    cv2.imshow('Result', img)
    cv2.waitKey(1)

