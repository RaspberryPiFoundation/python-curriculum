#!/bin/python3

# Code to draw a random-sized rectangle
  hideturtle()
  length = randint(10, 100)
  height = randint(10, 100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()
  
# Code to draw a star
  begin_fill()
  for side in range(5):
    left(144)
    forward(50)
  end_fill()
  