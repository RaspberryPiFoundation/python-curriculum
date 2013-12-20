from tkinter import *
import random 

main = Tk()

c = Canvas(main, width=600, height=600)
c.pack()

xpos = 60
ypos = 300


size = 10
walls = []
blocks = []


def setup():
    global walls, blocks, ypos, distance
    walls = []

    x = 0
    y = 0
    for i in range(600//size):
        y = y + random.randint(-5,5)
        if y < 0:
            y = 0
        x = x + size
        walls.append([x, y])

    blocks = []
    for i in range(6):
        x = i * 100
        y = random.randint(000,600)
        height = random.randint(size,size*5)
        blocks.append([x, y, height])

    ypos = 300
    distance = 0


playing = False
gravity = 5
distance = 0

def click(event):
    global playing, gravity
    if playing:
        gravity = -5
    else:
        playing = True
        setup()
        draw()

def release(event):
    global gravity
    gravity = 5

 
def draw():        
    global ypos, playing, distance
    global walls, blocks

    ypos = ypos + gravity
    distance = distance + size

    newwalls = []
    for x,y in walls:
        x = x-size
        if x >0:
            newwalls.append([x,y])
        else:
            walls.append([600,y+random.randint(-5,5)])
            
        if (x <= xpos < x+size) and (ypos<=100-y or ypos+size>= 600-y):
            playing = False
            
    walls = newwalls
        
    newblocks = []
    for x,y,h in blocks:
        x = x - size
        if x > 0:
            newblocks.append([x,y,h])
        else:
            newblocks.append([600, random.randint(0,600), random.randint(size,size*5)])
        if (x <= xpos < x+size) and (y <= ypos < y+h):
            playing = False
    blocks = newblocks

    c.delete(ALL)

    for x,y in walls:
        c.create_rectangle(x,600-y,x+size,600,fill="black")
        c.create_rectangle(x,0,x+size,100-y, fill="black")


    for x,y,height in blocks:
        c.create_rectangle(x,y,x+size,y+height,fill="black")


    if playing:
        c.create_rectangle(xpos,ypos,xpos+size,ypos+size, fill="black")
        c.after(15, draw)
    else:
        c.create_rectangle(xpos,ypos,xpos+size,ypos+size, fill="red")
        c.create_text(xpos, 300, text=str(distance), fill="red")
        print(distance)

c.bind("<Button-1>", click)
c.bind("<ButtonRelease-1>", release)
mainloop()
