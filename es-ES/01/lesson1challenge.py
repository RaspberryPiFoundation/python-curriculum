from turtle import *

speed(0)
shape("turtle")

def shape(lados, distancia, angulo):
    for count in range(lados):
        forward(distancia)
        right(angulo)


shape(5, 100, 360/5)
