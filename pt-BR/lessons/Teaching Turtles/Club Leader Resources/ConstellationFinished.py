from turtle import *
from random import *

#uma função para mover a tartaruga para uma posição aleatória
def moveToRandomLocation():
    penup()
    setpos( randint(-400,400) , randint(-400,400) )
    pendown()

#uma função para desenhar uma estrela de um tamanho específico
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

#uma função para desenhar uma pequena galáxia de estrelas
def drawGalaxy(numberOfStars):
    starColours = ["#058396","#0275A6","#827E01"]
    moveToRandomLocation()
    #desenha várias pequenas estrelas coloridas
    for star in range(numberOfStars):
        penup()
        left( randint(-180,180) )
        forward( randint(5,20) )
        pendown()       
        #desenha uma pequena estrela de cor aleatória
        drawStar( 2, choice(starColours) )

#uma função para desenhar uma constelação de estrelas
def drawConstellation(numberOfStars):
    moveToRandomLocation()
    #primeiro desenhamos todas as estrelas, exceto a última,
	#conectadas por linhas, assim: *--*--*--
    for star in range(numberOfStars-1):
        drawStar( randint(7,15) , "white")
        pendown()
        left( randint(-90,90) )
        forward( randint(30,70) )
    #agora desenhamos a última estrela
    drawStar( randint(7,15) , "White")

speed(11)

#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")

#desenha 30 estrelas brancas (tamanhos/posições aleatórias)
for star in range(30):
    moveToRandomLocation()
    drawStar( randint(5,25) , "White")

#desenha 3 pequenas galáxias de 40 estrelas
for galaxy in range(3):
    drawGalaxy(40)

#desenha 2 constelações, cada uma com um número aleatório de estrelas
for constellation in range(2):
    drawConstellation(randint(4,7))

hideturtle()
done()
