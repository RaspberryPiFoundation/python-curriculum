from turtle import *
from random import *

#a function for moving the turtle to a random location
def moveToRandomLocation():
    penup()
    setpos( randint(-400,400) , randint(-400,400) )
    pendown()

#a function for drawing a star of a particular size
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

#a function for drawing a small galaxy of stars
def drawGalaxy(numberOfStars):
    starColours = ["#058396","#0275A6","#827E01"]
    moveToRandomLocation()
    #draw lots of small coloured stars
    for star in range(numberOfStars):
        penup()
        left( randint(-180,180) )
        forward( randint(5,20) )
        pendown()       
        #draw a small star in a random colour
        drawStar( 2, choice(starColours) )

#a function for drawing a joined constellation of stars
def drawConstellation(numberOfStars):
    moveToRandomLocation()
    #first draw all stars except the last one,
    #joined by lines, like this: *--*--*--
    for star in range(numberOfStars-1):
        drawStar( randint(7,15) , "white")
        pendown()
        left( randint(-90,90) )
        forward( randint(30,70) )
    #now draw the last star
    drawStar( randint(7,15) , "White")

speed(11)

#this will draw a dark blue background
bgcolor("MidnightBlue")

#draw 30 white stars (random sizes/locations)
for star in range(30):
    moveToRandomLocation()
    drawStar( randint(5,25) , "White")

#draw 3 small galaxies of 40 stars
for galaxy in range(3):
    drawGalaxy(40)

#draw 2 constellations, each with a random number of stars
for constellation in range(2):
    drawConstellation(randint(4,7))

hideturtle()
done()
