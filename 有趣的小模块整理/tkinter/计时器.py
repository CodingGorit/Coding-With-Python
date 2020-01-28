# 时钟计时
import tkinter
import time

class App():
    def __init__(self):
        self.root = tkinter.Tk()
        self.label = tkinter.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text="当前系统时间:{}".format(now))
        self.root.after(1000, self.update_clock)

app=App()