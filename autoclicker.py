from cProfile import label
from cgitb import grey
import time,pyautogui,threading
import black
from turtle import width
from pynput.keyboard import Key, Controller
import keyboard
from tkinter import *

window = Tk()

window.title("AutoClilcker")
def startclicking():
    time.sleep(1)
    run=True
    interval=None
    #print(x.get(),'\n')
    try:
        interval=float(x.get())
        #print(interval,'\n')
    except:
        pass
    timer=time.time()
    #print(timer,'\n')
    while run:
        if keyboard.is_pressed("r"):
            run=False
            break
        if interval!=None:
            if time.time()>=(timer+interval):
                pyautogui.click()
                timer=time.time()
        else :
            pyautogui.click()

lbl = Label(window, text="autoclicker",justify='center')
lbl.grid(column=1,row=0, padx=(75,10))
window.geometry('500x200')

x=Entry(window,width=40)
x.grid(column=1,row=3, padx=(75,50), pady=(10,15))

button=Button(window,text="start clicking",command=startclicking,bg="grey",fg="black")
button.grid(column=1,row=4, padx=(75,10))


window.mainloop()