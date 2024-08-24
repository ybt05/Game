import tkinter as tk

class circle:
    def __init__(self):
        self.x0 = 20
        self.x1 = 70
        self.y0 = 20
        self.y1 = 70
        self.enter = 0
        self.out = 0
        self.clear = 0
    def reset(self):
        self.x0 = 20
        self.x1 = 70
        self.y0 = 20
        self.y1 = 70
        self.out = 0

root=tk.Tk()
fontName = "HGS創英角ﾎﾟｯﾌﾟ体"
circle1 = circle()