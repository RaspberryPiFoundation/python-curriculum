## this is at the top of every turtle file

from turtle import *

speed(0)

shape("turtle")
"""
### then first step is things like drawing a square

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

clear()

### then drawing a square through a for loop

for count in range(4):
    forward(100)
    right(90)

### making a function

def square():
    for count in range(4):
        forward(100)
        right(90)


square()

### making a better function

def square(length):
    for count in range(4):
        forward(length)
        right(90)


square(100)

### then let's draw a shape

def shape(sides, length, angle):
    for count in range(sides):
        forward(length)
        right(angle)


shape(5, 100, 360/5)

# can you draw a triangle, a hexagon, a pentagon?

# try and write the following shapre function that works out the angle.

def shape(sides, length):
    angle = 360/sides
    for count in range(sides):
        forward(length)
        right(angle)

shape(23, 5)


### fractals.

# let's draw a snowflake

# level 0
forward(100)

penup(); backward(100); right(90); forward(80); left(90); pendown();


# level 1
forward(30)
left(60)
forward(30)
right(120)
forward(30)
left(60)
forward(30)

penup(); backward(100); right(90); forward(80); left(90); pendown();


# level 2
forward(10)
left(60)
forward(10)
right(120)
forward(10)
left(60)
forward(10)
left(60)
forward(10)
left(60)
forward(10)
right(120)
forward(10)
left(60)
forward(10)
right(120)
forward(10)
left(60)
forward(10)
right(120)
forward(10)
left(60)
forward(10)
left(60)
forward(10)
left(60)
forward(10)
right(120)
forward(10)
left(60)
forward(10)

# this sucks, let's try again

# recursion.

def line(depth, length):
    if depth == 0:
        forward(length)
    else:
        line(depth-1, length)
        left(60)
        line(depth-1, length)
        right(120)
        line(depth-1, length)
        left(60)
        line(depth-1, length)

line(2,1)


def snowflake(depth, length):
    line(depth, length)
    right(120)
    line(depth, length)
    right(120)
    line(depth, length)
    right(120)

snowflake(2, 5)

reset()

# challenge, replace line with a new fractal

# from ____ ---> _/\_
#                  _
# to   ____ ---> _| |_

# makes the X fractal.

def line(depth, length):
    if depth == 0:
        forward(length)
    else:
        line(depth-1, length)
        left(90)
        line(depth-1, length)
        right(90)
        line(depth-1, length)
        right(90)
        line(depth-1, length)
        left(90)
        line(depth-1, length)


#line(2,5)

speed(999)


# however we can draw it in a square, instead of a triangle
# this is called the x-fractal

def xfractal(depth, length):
    line(depth, length)
    left(90)
    line(depth, length)
    left(90)
    line(depth, length)
    left(90)
    line(depth, length)
    left(90)

#xfractal(2,2)


reset()

speed(0)


# zelda/triforce fractal
# we're going to have to illustrate these

def triforce(depth, length):

    if depth == 0:
        pendown()
        forward(length)
        left(120)
        forward(length)
        left(120)
        forward(length)
        left(120)
        penup()
    else:
        penup()
        newlength = length/2
        newdepth = depth - 1
        triforce(newdepth, newlength)
        forward(newlength)
        triforce(newdepth, newlength)
        left(120)
        forward(newlength)
        right(120)
        triforce(newdepth, newlength)
        right(120)
        forward(newlength)
        left(120)

reset()
speed(0)
penup()
setpos(-255,-255)
triforce(7, 512)

"""

def bubble(depth, length):
    if depth == 0:
        pendown()
        circle(length/2)
        penup()
    else:
        penup()
        newlength = length/2
        newdepth = depth - 1
        bubble(newdepth, newlength)
        forward(newlength)
        bubble(newdepth, newlength)
        left(120)
        forward(newlength)
        right(120)
        bubble(newdepth, newlength)
        right(120)
        forward(newlength)
        left(120)

reset()
speed(0)
penup()
setpos(-255,-255)
bubble(6, 512)
