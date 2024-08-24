import threading
from values import *
import audio

def frame_0():
    frame0 = tk.Frame(root, background="#111111")
    frame0.place(relwidth=1, relheight=1)
    frame0.lift()
    lab0_1 = tk.Label(
        frame0, text="イライラ迷路", font=(fontName, 20), background="#111111", foreground="#DDDDDD"
    )
    lab0_1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    lab0_2 = tk.Label(
        frame0, text="Enter to Start", font=(fontName, 15), background="#111111", foreground="#DDDDDD"
    )
    lab0_2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    root.bind("<Key-Return>", display1)

def frame_1():
    frame1 = tk.Frame(root, background="#111111")
    frame1.place(relwidth=1, relheight=1)
    canvas1 = tk.Canvas(frame1, background="#111111")
    canvas1.place(relwidth=1, relheight=1)
    canvas1.create_rectangle(90, 0, 100, 400,fill="#DDDDDD",outline="#DDDDDD")
    canvas1.create_rectangle(190, 100, 200, 500,fill="#DDDDDD",outline="#DDDDDD")
    canvas1.create_rectangle(290, 0, 300, 400,fill="#DDDDDD",outline="#DDDDDD")
    canvas1.create_rectangle(390, 100, 400, 500,fill="#DDDDDD",outline="#DDDDDD")
    canvas1.create_oval(circle1.x0, circle1.y0, circle1.x1, circle1.y1,fill="#DDDDDD",outline="#DDDDDD")
    if circle1.enter==0:
        lab1_1 = tk.Label(
            frame1, text="Enter to Start", font=(fontName, 20), background="#111111", foreground="#DDDDDD" , height = 3
        )
        lab1_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    lab1_2 = tk.Label(
        frame1, text="Goal", font=(fontName, 15), background="#111111", foreground="#DDDDDD"
    )
    lab1_2.place(relx=0.9, rely=0.95, anchor=tk.CENTER)
    frame1.lift()
    if circle1.enter == 1:
        root.bind("<Key-s>", down)
        root.bind("<Key-w>", up)
        root.bind("<Key-d>", right)
        root.bind("<Key-a>", left)
        root.bind("<Key-Return>", nothing)
    else:
        root.bind("<Key-Return>", call)

def nothing(event):
    pass

def frame_2():
    frame2 = tk.Frame(root,background="#111111")
    frame2.place(relwidth=1, relheight=1)
    lab2_1 = tk.Label(
        frame2, text="Clear", font=(fontName, 20), background="#111111", foreground="#DDDDDD"
    )
    lab2_1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    lab2_2 = tk.Label(
        frame2, text="Enter to Quit", font=(fontName, 15), background="#111111", foreground="#DDDDDD"
    )
    lab2_2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    frame2.lift()
    root.bind("<Key-Return>", dest)

def judge():
    if circle1.y1 > 500 and circle1.x0 > 400 and circle1.x1 < 500:
        circle1.clear=1
    else:
        if circle1.y0 < 0 or circle1.x0 < 0:
            circle1.out = 1
        if circle1.y1 > 500 or circle1.x1 > 500:
            circle1.out = 1
        if circle1.y0 < 400 and circle1.x1 > 90 and circle1.x0 < 100:
            circle1.out = 1
        if circle1.y1 > 100 and circle1.x1 > 190 and circle1.x0 < 200:
            circle1.out = 1
        if circle1.y0 < 400 and circle1.x1 > 290 and circle1.x0 < 300:
            circle1.out = 1
        if circle1.y1 > 100 and circle1.x1 > 390 and circle1.x0 < 400:
            circle1.out = 1
    if circle1.out == 1:
        audio.outWav.play()
        circle1.reset()

def timeEvent():
    if circle1.clear==0:
        circle1.y0 = circle1.y0 - 3
        circle1.y1 = circle1.y1 - 3
        judge()
        th = threading.Thread(target=frame_1)
        th.start()
        root.after(100, timeEvent)
    else:
        clear()

def down(event):
    if circle1.clear==0:
        circle1.y0 = circle1.y0 + 10
        circle1.y1 = circle1.y1 + 10
        frame_1()

def up(event):
    if circle1.clear==0:
        circle1.y0 = circle1.y0 - 10
        circle1.y1 = circle1.y1 - 10
        frame_1()

def right(event):
    if circle1.clear==0:
        circle1.x0 = circle1.x0 + 10
        circle1.x1 = circle1.x1 + 10
        frame_1()

def left(event):
    if circle1.clear==0:
        circle1.x0 = circle1.x0 - 10
        circle1.x1 = circle1.x1 - 10
        frame_1()

def display1(event):
    audio.startWav.play()
    frame_1()

def call(event):
    circle1.enter = 1
    timeEvent()

def clear():
    audio.finishWav.play()
    frame_2()

def dest(event):
    root.destroy()