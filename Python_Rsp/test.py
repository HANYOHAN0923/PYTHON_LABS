import tkinter
import time
import random

window = tkinter.Tk()
window.title("반응속도 테스트")
window.geometry("640x380")

def gameStart():
    time.sleep(random.randrange(1,5))
    pressButton = tkinter.Button(window, text = 'Press Me', bg = 'green', command = gameEnd)

def gameEnd():
    timeText = tkinter.Label(window, text = pressButton.time(), font = (None,80))
    timeText.pack()

timeText = tkinter.Label(window, text = '0', font = (None,80))
timeText.pack()

pressButton = tkinter.Button(window, text = 'Start', bg = 'red', command = gameStart)
pressButton.pack()

window.mainloop()