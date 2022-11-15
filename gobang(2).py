from PIL import ImageTk,Image
import tkinter as tk

_al = []
_white = []
_black = []
stop = 0
boss = True
black = True

def get_image(filename,width,height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)
def init():
    global black,window,canvas
    window = tk.Tk()
    window.title('五子棋')
    window.geometry('850x600') #（）内写*报错

    #black = True
    canvas = tk.Canvas(window,  height=600, width=850)



    for i in range(1,16):
        line = canvas.create_line(i*40, 20, i*40, 580)
        line = canvas.create_line(40, i*40-20, 600, i*40-20)
        rect = canvas.create_rectangle(35, 15, 605, 585) #边框
        rect = canvas.create_rectangle(34, 14, 606, 586) #加粗

        oval = canvas.create_oval(157, 137, 163, 143, fill='black')
        oval = canvas.create_oval(157, 457, 163, 463, fill='black')
        oval = canvas.create_oval(477, 137, 483, 143, fill='black')
        oval = canvas.create_oval(477, 457, 483, 463, fill='black')
        oval = canvas.create_oval(315, 296, 325, 304, fill='black')
        #canvas.pack()

    end = tk.Button(window, text='结束游戏', bg='white', font=('Arial', 12), width=15, height=2,command=on_end)
    end.place(x=650,y=460,anchor='nw')  #结束游戏——>end

    start = tk.Button(window, text='重新开始', bg='white', font=('Arial', 12), width=15, height=2,command=on_start)
    start.place(x=650,y=300,anchor='nw')   #重新开始——>start

    regret = tk.Button(window, text='悔棋', bg='white', font=('Arial', 12), width=15, height=2,command=on_regret)
    regret.place(x=650,y=380,anchor='nw')  #悔棋——>regret
    canvas.pack()

def on_regret():
   
    global _al,_black,_white,black,_start
    _start = False
    _al.pop()
    if black == True:
        _white.pop()
        black = False
            
    else:
        _black.pop()

        black = True
    print(black)

    window.destroy()
    
    #悔棋——>regret
def on_start():
    global _start,_al,_black,_white
    _start = False
    del _al,_black,_white
    _al = []
    _white = []
    _black = []

    window.destroy()        #重新开始——>start

def on_end():
    #print(_white)
    global boss,_start
    boss = False
    _start = False
    window.destroy()    #结束游戏——>end

def win():      #检测胜负
    global stop
    temp1 = 0
    temp2=0
    for i in range(0,16):
        for j in range(0,16):
            if [i,j] in _black:
                temp1 = temp1 + 1
                if temp1 == 5:
                    stop = 1
                    return 'black'
            else:
                temp1 = 0   #检查行
            if [i,j] in _white:
                temp2 = temp2 + 1
                if temp2 == 5:
                    stop = 1
                    return 'white'
            else:
                temp2 = 0

    for i in range(0,16):
        for j in range(0,16):
            if [j,i] in _black:
                temp1 = temp1 + 1
                if temp1 == 5:
                    stop = 1
                    return 'black'
            else:
                temp1 = 0   #检查列
            if [j,i] in _white:
                temp2 = temp2 + 1
                if temp2 == 5:
                    stop = 1
                    return 'white'
            else:
                temp2 = 0

    for i in range(0,16):
        for j in range(0,16):
            if [i,j] in _black and [i+1,j+1] in _black and [i+2,j+2] in _black and [i+3,j+3] in _black and [i+4,j+4] in _black:
                stop = 1
                return 'black'
            if [i,j] in _white and [i+1,j+1] in _white and [i+2,j+2] in _white and [i+3,j+3] in _white and [i+4,j+4] in _white:
                stop = 1
                return 'white'

    for i in range(0,16):
        for j in range(0,16):
            if [i,j] in _black and [i+1,j-1] in _black and [i+2,j-2] in _black and [i+3,j-3] in _black and [i+4,j-4] in _black:
                stop = 1
                return 'black'
            if [i,j] in _white and [i+1,j-1] in _white and [i+2,j-2] in _white and [i+3,j-3] in _white and [i+4,j-4] in _white:
                stop = 1
                return 'white'

def callback(event):
    global _al,stop
    #print(event.x,event.y)
    x = (event.x+20)//40
    y = (event.y + 10)//40 + 1

  
    if event.x>=40 and event.x<=615 and event.y>=20 and event.y<=585 and stop == 0 :
        if [x,y] not in _al:
            _al.append([x,y])
            #print(_al)
        
            global black
            if black==True:
                black=False
                victory = tk.Label(window, text = '白子落子', bg='white', font=('Arial', 15), width=15, height=5)
                victory.place(x=650,y=100,anchor='nw')
                _black.append([x,y])
                oval = canvas.create_oval((event.x+20)//40*40-15,(event.y+8)//40*40+5, (event.x+20)//40*40+15, (event.y+8)//40*40+35, fill = 'black')
                canvas.pack()
            else:
                black=True
                victory = tk.Label(window, text = '黑子落子', bg='white', font=('Arial', 15), width=15, height=5)
                victory.place(x=650,y=100,anchor='nw')
                _white.append([x,y])
                oval = canvas.create_oval((event.x+20)//40*40-15,(event.y+8)//40*40+5, (event.x+20)//40*40+15, (event.y+8)//40*40+35, fill = 'white')
                canvas.pack()
            winner= win()
            if stop == 1:
                victory = tk.Label(window, text=winner + '获胜', bg='white', font=('Arial', 15), width=15, height=5)
                victory.place(x=650,y=100,anchor='nw')
            

while(boss):
    init()
    im = get_image("12.webp",850,600)
    canvas.create_image(428,300,image = im)
    stop = 0
    _start = True
    if black == True:
        victory = tk.Label(window, text = '黑子落子', bg='white', font=('Arial', 15), width=15, height=5)
        victory.place(x=650,y=100,anchor='nw')

    else:
        victory = tk.Label(window, text = '白子落子', bg='white', font=('Arial', 15), width=15, height=5)
        victory.place(x=650,y=100,anchor='nw')
  
        
    while(_start):
        for i in range(1,16):
            line = canvas.create_line(i*40, 20, i*40, 580)
            line = canvas.create_line(40, i*40-20, 600, i*40-20)
            rect = canvas.create_rectangle(35, 15, 605, 585) #边框
            rect = canvas.create_rectangle(34, 14, 606, 586) #加粗

            oval = canvas.create_oval(157, 137, 163, 143, fill='black')
            oval = canvas.create_oval(157, 457, 163, 463, fill='black')
            oval = canvas.create_oval(477, 137, 483, 143, fill='black')
            oval = canvas.create_oval(477, 457, 483, 463, fill='black')
            oval = canvas.create_oval(315, 296, 325, 304, fill='black')
        for i in _black:
            # print(i[0],i[1])
            oval = canvas.create_oval(i[0] * 40 - 15, i[1] * 40 - 35, i[0] * 40 + 15, i[1] * 40 - 5, fill='black')
            canvas.pack()
        for i in _white:
            # print(i[0],i[1])
            oval = canvas.create_oval(i[0] * 40 - 15, i[1] * 40 - 35, i[0] * 40 + 15, i[1] * 40 - 5, fill='white')
            canvas.pack()
        canvas.bind("<Button-1>",callback)
        canvas.pack()

        window.mainloop()
