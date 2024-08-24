import random
import audio
from values import *

def rand():
    if player.item == "メガネ" and cpu.item != "シールド":
        player.randWince = random.randint(1, 10)
        player.randCrit = random.randint(1, 10)
    if cpu.item == "メガネ" and player.item != "シールド":
        cpu.randWince = random.randint(1, 10)
        cpu.randWince = random.randint(1, 10)

def magnification_player():
    if player.type == "Flame":
        if cpu.type == "Flame":
            return 2
        if cpu.type == "Water":
            return 1
        if cpu.type == "Grass":
            return 4
    if player.type == "Water":
        if cpu.type == "Flame":
            return 4
        if cpu.type == "Water":
            return 2
        if cpu.type == "Grass":
            return 1
    if player.type == "Grass":
        if cpu.type == "Flame":
            return 1
        if cpu.type == "Water":
            return 4
        if cpu.type == "Grass":
            return 2

def magnification_cpu():
    if cpu.type == "Flame":
        if player.type == "Flame":
            return 2
        if player.type == "Water":
            return 1
        if player.type == "Grass":
            return 4
    if cpu.type == "Water":
        if player.type == "Flame":
            return 4
        if player.type == "Water":
            return 2
        if player.type == "Grass":
            return 1
    if cpu.type == "Grass":
        if player.type == "Flame":
            return 1
        if player.type == "Water":
            return 4
        if player.type == "Grass":
            return 2

def attack_player():
    if cpu.act == 1:
        cpu.hp = cpu.hp
    else:
        if cpu.item == "シールド":
            dmg = magnification_player() - 1
        else:
            dmg = magnification_player()
        cpu.hp = int(cpu.hp) - dmg
        if player.item == "メガネ" and cpu.item != "シールド":
            if player.randCrit == 1:
                cpu.hp = cpu.hp - 2
                cpu.critHit = 1

def attack_cpu():
    if player.act == 1:
        player.hp = player.hp
    else:
        if player.item == "シールド":
            dmg = magnification_cpu() - 1
        else:
            dmg = magnification_cpu()
        player.hp = player.hp - dmg
        if cpu.item == "メガネ" and player.item != "シールド":
            if cpu.randCrit == 1:
                player.hp = player.hp - 2
                player.critHit = 1

def cal():
    global turn
    rand()
    cpuAct()
    player.critHit = 0
    cpu.critHit = 0
    player.potionUse = 0
    cpu.potionUse = 0
    if player.act == 0:
        if cpu.randWince != 1:
            attack_player()
    if cpu.act == 0:
        if player.randWince != 1:
            attack_cpu()
    if player.hp <= 0 and cpu.hp <= 0:
        cpu.win = 1
        player.win = 1
        frame_5()
    elif player.hp <= 0:
        cpu.win = 1
        frame_5()
    elif cpu.hp <= 0:
        player.win = 1
        frame_5()
    else:
        if player.item == "ポーション" and player.potion != 0:
            if player.hp <= 7:
                player.hp = player.hp + 4
                player.potion = player.potion - 1
                player.potionUse = 1
        if cpu.item == "ポーション" and cpu.potion != 0:
            if cpu.hp <= 7:
                cpu.hp = cpu.hp + 4
                cpu.potion = cpu.potion - 1
                cpu.potionUse = 1
        if player.item == "リジェネバンド" and player.hp != 15 and turn % 2 == 0:
            player.hp = player.hp + 1
        if cpu.item == "リジェネバンド" and cpu.hp != 15 and turn % 2 == 0:
            cpu.hp = cpu.hp + 1
        frame_5()
    turn = turn + 1

def flame():
    audio.button2Wav.play()
    player.type = "Flame"
    player.color = "#FF8844"
    player.act = 2
    player.push = 1

def water():
    audio.button2Wav.play()
    player.type = "Water"
    player.color = "#6666FF"
    player.act = 2
    player.push = 1

def grass():
    audio.button2Wav.play()
    player.type = "Grass"
    player.color = "#66FF66"
    player.act = 2
    player.push = 1

def display1(event):
    audio.startWav.play()
    frame_1()

def display2(name):
    audio.button1Wav.play()
    global playerName
    playerName = name
    if playerName != "":
        frame_2()

def display3():
    audio.button1Wav.play()
    if player.type != "":
        frame_3()

def display4(item):
    audio.button1Wav.play()
    player.item = item
    frame_4()

def display4_2(event):
    if player.win == 1 or cpu.win == 1:
        audio.finishWav.play()
        frame_6()
    else:
        frame_4()

def dest(event):
    root.destroy()

def attack():
    audio.button2Wav.play()
    player.act = 0
    player.push = 1

def protect():
    audio.button2Wav.play()
    player.act = 1
    player.prot = player.prot - 1
    player.push = 1

def decision():
    audio.button1Wav.play()
    if player.push == 1:
        cal()

def frame_0():
    frame0 = tk.Frame(root, background="#DDEEFF")
    frame0.place(relwidth=1, relheight=1)
    frame0.lift()
    lab0_1 = tk.Label(
        frame0, text="Element Monster", font=(fontName, 20), background="#DDEEFF"
    )
    lab0_1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    lab0_2 = tk.Label(
        frame0, text="Click to Start", font=(fontName, 15), background="#DDEEFF"
    )
    lab0_2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    frame0.bind("<Button-1>", display1)

def frame_1():
    frame1 = tk.Frame(root, background="#DDEEFF")
    frame1.place(relwidth=1, relheight=1)
    frame1.lift()
    lab1_1 = tk.Label(
        frame1, text="名前を入力してください", font=(fontName, 20), background="#DDEEFF"
    )
    lab1_1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entry1_1 = tk.Entry(frame1,textvariable=name)
    entry1_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button2_1 = tk.Button(
        frame1,
        text="決定",
        bg="#BBBBBB",
        width=10,
        height=2,
        activebackground="#666666",
        font=(fontName, 10),
        command=lambda: display2(name.get()),
    )
    button2_1.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def frame_2():
    frame2 = tk.Frame(root, background="#DDEEFF")
    frame2.place(relwidth=1, relheight=1)
    frame2.lift()
    lab2_1 = tk.Label(
        frame2,
        text="最初の属性を選んでください",
        font=(fontName, 20),
        background="#DDEEFF",
    )
    lab2_1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    button2_1 = tk.Button(
        frame2,
        text="ほのお",
        bg="#FF8844",
        width=10,
        height=2,
        activebackground="#DD6622",
        font=(fontName, 10),
        command=flame,
    )
    button2_1.place(relx=0.25, rely=0.7, anchor=tk.CENTER)
    button2_2 = tk.Button(
        frame2,
        text="みず",
        bg="#6666FF",
        width=10,
        height=2,
        activebackground="#4444DD",
        font=(fontName, 10),
        command=water,
    )
    button2_2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    button2_3 = tk.Button(
        frame2,
        text="くさ",
        bg="#66FF66",
        width=10,
        height=2,
        activebackground="#44DD44",
        font=(fontName, 10),
        command=grass,
    )
    button2_3.place(relx=0.75, rely=0.7, anchor=tk.CENTER)
    button2_4 = tk.Button(
        frame2,
        text="決定",
        bg="#BBBBBB",
        width=10,
        height=2,
        activebackground="#666666",
        font=(fontName, 10),
        command=display3,
    )
    button2_4.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def frame_3():
    frame3 = tk.Frame(root, background="#DDEEFF")
    frame3.place(relwidth=1, relheight=1)
    frame3.lift()
    lab3_1 = tk.Label(
        frame3,
        text="アイテムを選んでください",
        font=(fontName, 20),
        background="#DDEEFF",
    )
    lab3_1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    item_list = ["アイテムなし", "ポーション", "メガネ", "シールド", "リジェネバンド"]
    comb3_1 = ttk.Combobox(
        frame3, values=item_list, textvariable=item, state="readonly"
    )
    comb3_1.set("アイテムなし")
    comb3_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button3_1 = tk.Button(
        frame3,
        text="決定",
        bg="#BBBBBB",
        width=10,
        height=2,
        activebackground="#666666",
        font=(fontName, 10),
        command=lambda: display4(item.get()),
    )
    button3_1.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def frame_4():
    player.push = 0
    frame4 = tk.Frame(root, background="#DDEEFF")
    frame4.place(relwidth=1, relheight=1)
    frame4.lift()
    lab4_1 = tk.Label(
        frame4, text="行動を選択してください", font=(fontName, 20), background="#DDEEFF"
    )
    lab4_1.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    lab4_2 = tk.Label(
        frame4, text="属性変更", font=(fontName, 20), background="#DDEEFF"
    )
    lab4_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button4_1 = tk.Button(
        frame4,
        text="ほのお",
        bg="#FF8844",
        width=10,
        height=2,
        activebackground="#DD6622",
        font=(fontName, 10),
        command=flame,
    )
    if player.type != "Flame":
        button4_1.place(relx=0.25, rely=0.6, anchor=tk.CENTER)
    button4_2 = tk.Button(
        frame4,
        text="みず",
        bg="#6666FF",
        width=10,
        height=2,
        activebackground="#4444DD",
        font=(fontName, 10),
        command=water,
    )
    if player.type != "Water":
        button4_2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    button4_3 = tk.Button(
        frame4,
        text="くさ",
        bg="#66FF66",
        width=10,
        height=2,
        activebackground="#44DD44",
        font=(fontName, 10),
        command=grass,
    )
    if player.type != "Grass":
        button4_3.place(relx=0.75, rely=0.6, anchor=tk.CENTER)
    button4_4 = tk.Button(
        frame4,
        text="決定",
        bg="#BBBBBB",
        width=10,
        height=2,
        activebackground="#666666",
        font=(fontName, 10),
        command=decision,
    )
    button4_4.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    button4_4 = tk.Button(
        frame4,
        text="攻撃",
        bg="#BBBB44",
        width=10,
        height=2,
        activebackground="#888811",
        font=(fontName, 10),
        command=attack,
    )
    button4_4.place(relx=0.35, rely=0.35, anchor=tk.CENTER)
    if player.prot != 0:
        button4_4 = tk.Button(
            frame4,
            text="防御 " + str(player.prot),
            bg="#44BBBB",
            width=10,
            height=2,
            activebackground="#118888",
            font=(fontName, 10),
            command=protect,
        )
        button4_4.place(relx=0.65, rely=0.35, anchor=tk.CENTER)
    hp1.set(player.hp)
    pb4_1 = ttk.Progressbar(frame4, maximum=15, mode="determinate", variable=hp1)
    pb4_1.place(relx=0.22, rely=0.1, anchor=tk.CENTER)
    lab4_3 = tk.Label(
        frame4,
        text=playerName,
        font=(fontName, 10),
        background="#DDEEFF",
        foreground=player.color,
    )
    lab4_3.place(relx=0.06, rely=0.1, anchor=tk.CENTER)
    hp2.set(cpu.hp)
    pb4_2 = ttk.Progressbar(frame4, maximum=15, mode="determinate", variable=hp2)
    pb4_2.place(relx=0.78, rely=0.1, anchor=tk.CENTER)
    lab4_4 = tk.Label(
        frame4,
        text="CPU",
        font=(fontName, 10),
        background="#DDEEFF",
        foreground=cpu.color,
    )
    lab4_4.place(relx=0.92, rely=0.1, anchor=tk.CENTER)

def frame_5():
    frame5 = tk.Frame(root, background="#DDEEFF")
    frame5.place(relwidth=1, relheight=1)
    frame5.lift()
    hp1.set(player.hp)
    pb5_1 = ttk.Progressbar(frame5, maximum=15, mode="determinate", variable=hp1)
    pb5_1.place(relx=0.22, rely=0.1, anchor=tk.CENTER)
    lab5_1 = tk.Label(
        frame5,
        text=playerName,
        font=(fontName, 10),
        background="#DDEEFF",
        foreground=player.color,
    )
    lab5_1.place(relx=0.06, rely=0.1, anchor=tk.CENTER)
    hp2.set(cpu.hp)
    pb5_2 = ttk.Progressbar(frame5, maximum=15, mode="determinate", variable=hp2)
    pb5_2.place(relx=0.78, rely=0.1, anchor=tk.CENTER)
    lab5_2 = tk.Label(
        frame5,
        text="CPU",
        font=(fontName, 10),
        background="#DDEEFF",
        foreground=cpu.color,
    )
    lab5_2.place(relx=0.92, rely=0.1, anchor=tk.CENTER)
    if player.act == 0:
        lab5_3 = tk.Label(
            frame5,
            text=playerName+"は 攻撃 をした",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    if player.act == 1:
        lab5_3 = tk.Label(
            frame5,
            text=playerName+"は 防御 をした",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    if player.act == 2 and player.type == "Flame":
        lab5_3 = tk.Label(
            frame5,
            text=playerName+"は ほのお属性 になった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    if player.act == 2 and player.type == "Water":
        lab5_3 = tk.Label(
            frame5,
            text=playerName+"は みず属性 になった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    if player.act == 2 and player.type == "Grass":
        lab5_3 = tk.Label(
            frame5,
            text=playerName+"は くさ属性 になった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    lab5_3.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    if cpu.act == 0:
        lab5_4 = tk.Label(
            frame5, text="CPUは 攻撃 をした", font=(fontName, 20), background="#DDEEFF"
        )
    if cpu.act == 1:
        lab5_4 = tk.Label(
            frame5, text="CPUは 防御 をした", font=(fontName, 20), background="#DDEEFF"
        )
    if cpu.act == 2 and cpu.type == "Flame":
        lab5_4 = tk.Label(
            frame5,
            text="CPUは ほのお属性 になった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    if cpu.act == 2 and cpu.type == "Water":
        lab5_4 = tk.Label(
            frame5,
            text="CPUは みず属性 になった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    if cpu.act == 2 and cpu.type == "Grass":
        lab5_4 = tk.Label(
            frame5,
            text="CPUは くさ属性 になった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
    lab5_4.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    if cpu.randWince == 1 and player.act == 0:
        lab5_5 = tk.Label(
            frame5,
            text=playerName+"はひるんで動けなかった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
        lab5_5.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    if player.randWince == 1 and cpu.act == 0:
        lab5_6 = tk.Label(
            frame5,
            text="CPUはひるんで動けなかった",
            font=(fontName, 20),
            background="#DDEEFF",
        )
        lab5_6.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    if player.critHit == 1:
        lab5_7 = tk.Label(
            frame5, text="クリティカル", font=(fontName, 10), background="#DDEEFF"
        )
        lab5_7.place(relx=0.1, rely=0.15, anchor=tk.CENTER)
    if cpu.critHit == 1:
        lab5_8 = tk.Label(
            frame5, text="クリティカル", font=(fontName, 10), background="#DDEEFF"
        )
        lab5_8.place(relx=0.9, rely=0.15, anchor=tk.CENTER)
    if player.potionUse == 1:
        lab5_9 = tk.Label(
            frame5,
            text=playerName+"はポーションを使った",
            font=(fontName, 20),
            background="#DDEEFF",
        )
        lab5_9.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    if cpu.potionUse == 1:
        lab5_10 = tk.Label(
            frame5,
            text="CPUはポーションを使った",
            font=(fontName, 20),
            background="#DDEEFF",
        )
        lab5_10.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    frame5.bind("<Button-1>", display4_2)

def frame_6():
    frame6 = tk.Frame(root, background="#DDEEFF")
    frame6.place(relwidth=1, relheight=1)
    frame6.lift()
    if player.win == 1 and cpu.win == 1:
        lab6_1 = tk.Label(
            frame6, text=playerName+" and CPU", font=(fontName, 20), background="#DDEEFF"
        )
        lab6_1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    elif player.win == 1:
        lab6_1 = tk.Label(
            frame6, text=playerName, font=(fontName, 20), background="#DDEEFF"
        )
        lab6_1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    elif cpu.win == 1:
        lab6_2 = tk.Label(frame6, text="CPU", font=(fontName, 20), background="#DDEEFF")
        lab6_2.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    lab6_3 = tk.Label(
        frame6, text="The Winner is", font=(fontName, 20), background="#DDEEFF"
    )
    lab6_3.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    lab6_4 = tk.Label(
        frame6, text="Click to Quit", font=(fontName, 15), background="#DDEEFF"
    )
    lab6_4.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    frame6.bind("<Button-1>", dest)

def cpuColor():
    if cpu.type == "Flame":
        cpu.color = "#FF8844"
    if cpu.type == "Water":
        cpu.color = "#6666FF"
    if cpu.type == "Grass":
        cpu.color = "#66FF66"

def cpuChoice():
    cpu.type = random.choice(["Flame", "Water", "Grass"])
    cpuColor()
    cpu.item = random.choice(["アイテムなし", "ポーション", "メガネ", "シールド", "リジェネバンド"])

def cpuAct():
    if cpu.prot != 0:
        x = random.randint(1, 4)
        if x == 1 or x == 2:
            cpu.act = 0
        elif x == 3:
            cpu.act = 1
            cpu.prot = cpu.prot - 1
        else:
            x = random.randint(1, 2)
            cpu.act = 2
            if cpu.type == "Flame":
                if x == 1:
                    cpu.type = "Water"
                if x == 2:
                    cpu.type = "Grass"
            elif cpu.type == "Water":
                if x == 1:
                    cpu.type = "Flame"
                if x == 2:
                    cpu.type = "Grass"
            elif cpu.type == "Grass":
                if x == 1:
                    cpu.type = "Water"
                if x == 2:
                    cpu.type = "Flame"
    else:
        x = random.randint(1, 4)
        if x == 1 or x == 2 or x == 3:
            cpu.act = 0
        else:
            x = random.randint(1, 2)
            cpu.act = 2
            if cpu.type == "Flame":
                if x == 1:
                    cpu.type = "Water"
                if x == 2:
                    cpu.type = "Grass"
            elif cpu.type == "Water":
                if x == 1:
                    cpu.type = "Flame"
                if x == 2:
                    cpu.type = "Grass"
            elif cpu.type == "Grass":
                if x == 1:
                    cpu.type = "Water"
                if x == 2:
                    cpu.type = "Flame"
    cpuColor()