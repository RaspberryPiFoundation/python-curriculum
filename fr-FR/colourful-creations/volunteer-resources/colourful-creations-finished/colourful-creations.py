#!/bin/python3

from turtle import *
from time import *

# introduction aux dictionnaires
# utilise un sélecteur de couleur pour trouver et choisir de nouvelles couleurs
colours = { 
  'space': '#060608', 
  'moongrey': '#BCBDEF', 
  'verylime': '#A7E30E', 
  'deepsea': '#226363', 
  'reallyraspberry': '#FA057F', 
  'gloomygrey': '#363332', 
  'awesomeorange':  '#F37C06', 
  'coolcyan': '#4FEEF6',
  'perfectpurple': '#6820B0',
  'lovelylemon': '#FBF312',
}

screen = Screen()
screen.setup(420, 420)
screen.bgcolor(colours['space'])

penup()
goto(0, 100)
color(colours['reallyraspberry'])
style = ('Arial', 40, 'bold')
write('SALUT', font=style, align='center')
right(90)
forward(60)
color(colours['awesomeorange'])
write('LE MONDE', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['moongrey'])
dot(370)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['verylime'])
style=('Verdana', 20, 'bold')
write('Un', font=style, align='center')
forward(40)
color(colours['reallyraspberry'])
write('smartphone', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['deepsea'])
write('a plus de', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['awesomeorange'])
write('puissance de calcul', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['perfectpurple'])
write('que', font=style, align='center')
forward(40)
color(colours['coolcyan'])
write('Apollo 11', font=('Verdana', 25, 'bold'), align='center')
color(colours['lovelylemon'])
forward(40)
write('quand il a atteri sur', font=style, align='center')
color(colours['gloomygrey'])
forward(40)
write('la lune', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(65)
write('- Nancy Gibbs, 2012', font=('Arial', 14, 'normal'))
