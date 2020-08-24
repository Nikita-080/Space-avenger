from tkinter import *
import time
import random
from PIL import Image, ImageTk
import os
tk = Tk()
tk.title('Space avenger')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=700, highlightthickness=0, bg="black")
canvas.pack()
tk.update()
def start_game(event):
    global game,avenger,bullet_blue,bullet_green,enemy
    if game==False:
        canvas.delete(ALL)
        avenger=canvas.create_image(250,600,image=img1)
        bullet_green=[]
        bullet_blue=[]
        enemy=[]
        game=True
def end_game():
    canvas.delete(ALL)
    canvas.create_text(250,350,fill = 'red',text="Game over\nPress <Enter> to restart\nPress ← → to move\nPress <Q> or <W> to shoot")
def turn_right(event):
    if game==True:
        canvas.move(avenger, 7, 0)
def turn_left(event):
    if game==True:
        canvas.move(avenger, -7, 0)
def create_bullet_blue(event):
    global bullet_blue
    if game==True:
        x1,y1,x2,y2=canvas.bbox(avenger)
        bullet_blue.append(canvas.create_image(x1+30,y1-30,image=img2))
def create_bullet_green(event):
    global bullet_green
    if game==True:
        x1,y1,x2,y2=canvas.bbox(avenger)
        bullet_green.append(canvas.create_image(x1,y1-31,image=img3))
        bullet_green.append(canvas.create_image(x1+60,y1-31,image=img3))
def create_enemy():
    global enemy
    enemy.append([-1,True,canvas.create_image(34,26,image=img4)])
    canvas.move(enemy[-1][2],random.randint(0,500),-30)
way=os.getcwd().replace("\\","/")+"/"
img1=ImageTk.PhotoImage(Image.open(way+"avenger.png"))
img2=ImageTk.PhotoImage(Image.open(way+"plasma blue.png"))
img3=ImageTk.PhotoImage(Image.open(way+"plasma green.png"))
img4=ImageTk.PhotoImage(Image.open(way+"enemy1.png"))
img5=ImageTk.PhotoImage(Image.open(way+"enemy2.png"))
img6=ImageTk.PhotoImage(Image.open(way+"enemy3.png"))
img7=ImageTk.PhotoImage(Image.open(way+"enemy4.png"))
img8=ImageTk.PhotoImage(Image.open(way+"enemy5.png"))
img9=ImageTk.PhotoImage(Image.open(way+"enemy6.png"))
avenger=-1
bullet_blue=[]
bullet_green=[]
enemy=[]
count=0
game=False
canvas.create_text(250,350,fill = 'red',text="Welcome\nPress <Enter> to start\nPress ← → to move\nPress <Q> or <W> to shoot")
canvas.bind_all('<Right>', turn_right)
canvas.bind_all('<Left>', turn_left)
canvas.bind_all('<q>', create_bullet_blue)
canvas.bind_all('<w>', create_bullet_green)
canvas.bind_all('<Return>', start_game)
while True:
    if game==True:
        for i in bullet_blue:
            canvas.move(i,0,-10)
        for i in bullet_green:
            canvas.move(i,0,-5)
        for i in enemy:
            if i[0]==-1:
                canvas.move(i[2],0,2)
        count+=1
        if count==200:
            count=0
            create_enemy()
        for i in range(len(enemy)):
            if enemy[i][0]==-1:
                x1,y1,x2,y2=canvas.bbox(enemy[i][2])
                things=canvas.find_overlapping(x1,y1,x2,y2)
                for k in things:
                    if k==avenger:
                        game=False
                    elif k in bullet_blue:
                        canvas.delete(k)
                        bullet_blue.remove(k)
                        enemy[i][0]=50
                        canvas.itemconfigure(enemy[i][2], image=img5)
                    elif k in bullet_green:
                        canvas.delete(k)
                        bullet_green.remove(k)
                        enemy[i][0]=50
                        canvas.itemconfigure(enemy[i][2], image=img5)
                if y1>700:
                    canvas.delete(enemy[i][2])
                    enemy[i][1]=False
            else:
                enemy[i][0]-=1
                if enemy[i][0]==40:
                    canvas.itemconfigure(enemy[i][2], image=img6)
                if enemy[i][0]==30:
                    canvas.itemconfigure(enemy[i][2], image=img7)
                if enemy[i][0]==20:
                    canvas.itemconfigure(enemy[i][2], image=img8)
                if enemy[i][0]==10:
                    canvas.itemconfigure(enemy[i][2], image=img9)
                if enemy[i][0]==0:
                    canvas.delete(enemy[i][2])
                    enemy[i][1]=False
        enemy=list(filter(lambda x: x[1], enemy))    
        if game==False:
            end_game()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    
