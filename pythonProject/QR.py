import cv2

import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
while (True):
    b, img = cap.read()
    for barcode in decode(img):
        mydata = barcode.data.decode('UTF-8')
        print(mydata)
        p = np.array([barcode.polygon], np.int32)
        p = p.reshape((-1, 1, 2))
        cv2.polylines(img, [p], True, (255, 0, 255), 5)

        # print(barcode.data)
    cv2.imshow("result", img)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Escape hit,closing...")
        break
cap.release()
cv2.destroyAllWindows()