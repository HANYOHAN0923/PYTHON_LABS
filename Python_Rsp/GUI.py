#시작하기 누르면 버튼 빨간색에 초록색에 클릭하라고 말함
#동시에 5초 안에 임의로 버튼이 초록색으로 바뀜
#빨간색일 때 누르면 오류(다시)
#초록색일 때 누르면 ms 반환

import tkinter as tk
import time
import random

def startTimer():
    if(running):
        global timer
        timer += 1
        timeText.configure(text=str(timer))
    window.after(10,startTimer)
    
def start():
    global running
    running = True
    
def stop():
    global running
    running = False
    
running = False

window = tk.Tk()
window.title("반응속도 테스트")
window.geometry("1280x640")

timer = 0

timeText = tk.Label(window, text = '0', font = (None,80))
timeText.pack()

pressButton = tk.Button(window, text='Start', bg='red',command=start, width = 320, height = 240)

pressButton.pack()

pressButton = tk.Button(window, text = 'Stop', bg='green', command = stop, width = 320, height = 240)

pressButton.pack(fill = tk.BOTH)

startTimer()
window.mainloop()