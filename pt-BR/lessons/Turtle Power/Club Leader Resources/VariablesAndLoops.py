from turtle import *

speed(11)
shape("turtle")

lados = 12
angulo = 360 / lados

for count in range(lados):
    forward(100)
    left(angulo)
