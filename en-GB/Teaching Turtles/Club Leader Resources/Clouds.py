from random import *
from turtle import *

def gotoRandomPlace():
    penup()
    setpos( randint(-400, 400) , randint(-400, 400) )
    pendown()

def bird(size):
    color("black")
    grp()
    setheading(300)
    fd(size)
    left(120)
    fd(size)

def cloud():
    color("white")
    setheading(90)
    begin_fill()
    for t in range(3):
        left(90)
        for i in range(90):
            fd(1)
            right(2)
        
    
    end_fill()
    

speed(11)
bgcolor("lightblue")


for b in range(12):
    gotoRandomPlace()
    cloud()

for b in range(50):
    gotoRandomPlace()
    bird(10)

done()
