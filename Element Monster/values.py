import tkinter as tk
import tkinter.ttk as ttk

class PlayerData:
    def __init__(self):
        self.type = ""  # 属性
        self.item = ""  # アイテム
        self.hp = 15  # 体力
        self.prot = 2  # 防御の回数
        self.randWince = 0  # 怯みの乱数
        self.randCrit = 0  # 急所の乱数
        self.potion = 1  # ポーションの回数
        self.act = 0  # 行動(攻撃,防御,属性変更)
        self.color = "#000000"
        self.win = 0
        self.critHit = 0
        self.potionUse = 0
        self.push = 0

player = PlayerData()
cpu = PlayerData()
fontName = "HGS創英角ﾎﾟｯﾌﾟ体"
playerName = "Player"
root = tk.Tk()
hp1 = tk.IntVar()
hp2 = tk.IntVar()
item = tk.StringVar()
name = tk.StringVar()
turn = 1