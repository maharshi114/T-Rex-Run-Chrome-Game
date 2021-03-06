import numpy as np
import cv2
from mss import mss
from PIL import Image                                                                                
import keyboard
from time import sleep 
mon1 = {'top': 200, 'left': 160, 'width': 800, 'height': 200}
sct1 = mss()
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (50,50)
fontScale              = 1
fontColor              = (255,0,0)
lineType               = 2
xcnts = []                                                                                                                          
count = 0
last_count = 0
while 1:
    #sleep(0.0001)
    sct1.get_pixels(mon1)
    img1 = Image.frombytes('RGB', (sct1.width, sct1.height), sct1.image)
    img_arry1 = np.array(img1)
    obj2 = img_arry1[125:155 , 110:155]
    gray = cv2.cvtColor(obj2, cv2.COLOR_BGR2GRAY)  
    th, threshed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU) 
    cnts = cv2.findContours(threshed, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2] 
    count = len(cnts)
    if count >= 1:
        keyboard.press_and_release('space')
        keyboard.press_and_release('space')
    cv2.putText(img_arry1,str(count), bottomLeftCornerOfText, font, fontScale,fontColor, lineType)
    cv2.imshow('test1', np.array(img_arry1))
    cv2.imshow('Obj2', np.array(gray))
    cv2.imshow('cnts', np.array(threshed))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
