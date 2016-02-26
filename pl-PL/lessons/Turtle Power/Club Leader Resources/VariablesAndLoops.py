from turtle import *

speed(11)
shape("turtle")

sides = 12
angle = 360 / sides

for count in range(sides):
    forward(100)
    left(angle)
