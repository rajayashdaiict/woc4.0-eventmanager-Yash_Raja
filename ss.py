import numpy as np
import cv2
import pyautogui
import os
import keyboard

while True:
    if keyboard.is_pressed("r"):    # R to capture screen 
        # take screenshot using pyautogui
        image = pyautogui.screenshot()

        image = cv2.cvtColor(np.array(image),
                            cv2.COLOR_RGB2BGR)

        #file handling part   
        # writing it to the disk using opencv
        a=int(1)
        s="image"+str(a)+".png"
        #print(s)
        #if file name is exist it will create a new name each time with having prefix "image"
        while True:
            if os.path.isfile('./'+s) :
                a=a+1
                s="image"+str(a)+".png"
            else :
                cv2.imwrite(s, image)
                break
    elif keyboard.is_pressed("s") :     #s to exit the code 
        break
    
