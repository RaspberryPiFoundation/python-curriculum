#!/bin/python3

#############
# CodeCraft #
#############

#---
#Game functions
#---

#moves the player left 1 tile.
def moveLeft():
  global playerX
  if(playerX > 0):
    playerX -= 1
    drawPlayer()

#moves the player right 1 tile.
def moveRight():
  global playerX, MAPWIDTH
  if(playerX < MAPWIDTH - 1):
    playerX += 1
    drawPlayer()

#moves the player up 1 tile.
def moveUp():
  global playerY
  if(playerY > 0):
    playerY -= 1
    drawPlayer()

#moves the player down 1 tile.
def moveDown():
  global playerY, MAPHEIGHT
  if(playerY < MAPHEIGHT - 1):
    playerY += 1
    drawPlayer()

#picks up the resource at the player's position.
def pickUp():
  global playerX, playerY
  drawing = True
  currentTile = world[playerX][playerY]
  #if the user doesn't already have too many...
  if inventory[currentTile] < MAXTILES:
    #player now has 1 more of this resource
    inventory[currentTile] += 1
    #the player is now standing on dirt
    world[playerX][playerY] = DIRT
    #draw the new DIRT tile
    drawResource(playerX, playerY)
    #redraw the inventory with the extra resource.
    drawInventory()

#place a resource at the player's current position
def place(resource):
  print('placing: ', names[resource])
  #only place if the player has some left...
  if inventory[resource] > 0:
    #find out the resourcee at the player's current position
    currentTile = world[playerX][playerY]
    #pick up the resource the player's standing on
    #(if it's not DIRT)
    if currentTile is not DIRT:
      inventory[currentTile] += 1
    #place the resource at the player's current position
    world[playerX][playerY] = resource
    #add the new resource to the inventory
    inventory[resource] -= 1
    #update the display (world and inventory)
    drawResource(playerX, playerY)
    drawInventory()
    print('   Placing', names[resource], 'complete')
  #...and if they have none left...
  else:
    print('   You have no', names[resource], 'left')

#craft a new resource
def craft(resource):
  print('Crafting: ', names[resource])
  #if the resource can be crafted...
  if resource in crafting:
    #keeps track of whether we have the resources
    #to craft this item
    canBeMade = True
    #for each item needed to craft the resource
    for i in crafting[resource]:
      #...if we don't have enough...
      if crafting[resource][i] > inventory[i]:
      #...we can't craft it!
        canBeMade = False
        break
    #if we can craft it (we have all needed resources)
    if canBeMade == True:
      #take each item from the inventory
      for i in crafting[resource]:
        inventory[i] -= crafting[resource][i]
      #add the crafted item to the inventory
      inventory[resource] += 1
      print('   Crafting', names[resource], 'complete')
    #...otherwise the resource can't be crafted...
    else:
      print('   Can\'t craft', names[resource])
    #update the displayed inventory
    drawInventory()

#creates a function for placing each resource
def makeplace(resource):
  return lambda: place(resource)

#attaches a 'placing' function to each key press
def bindPlacingKeys():
  for k in placekeys:
    screen.onkey(makeplace(k), placekeys[k])

#creates a function for crafting each resource
def makecraft(resource):
  return lambda: craft(resource)

#attaches a 'crafting' function to each key press
def bindCraftingKeys():
  for k in craftkeys:
    screen.onkey(makecraft(k), craftkeys[k])

#draws a resource at the position (y,x)
def drawResource(y, x):
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #draw the resource at that position in the tilemap, using the correct image
    rendererT.goto( (y * TILESIZE) + 20, height - (x * TILESIZE) - 20 )
    #draw tile with correct texture
    texture = textures[world[y][x]]
    rendererT.shape(texture)
    rendererT.stamp()
    screen.update()
    #nothing is now being drawn
    drawing = False

#draws the player on the world
def drawPlayer():
  playerT.goto( (playerX * TILESIZE) + 20, height - (playerY * TILESIZE) -20 )

#draws the world map
def drawWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in the row
    for column in range(MAPWIDTH):
      #draw the tile at the current position
      drawResource(column, row)

#draws the inventory to the screen
def drawInventory():
  #this variable stops other stuff being drawn
  global drawing
  #only draw if nothing else is being drawn
  if drawing == False:
    #something is now being drawn
    drawing = True
    #use a rectangle to cover the current inventory
    rendererT.color(BACKGROUNDCOLOUR)
    rendererT.goto(0,0)
    rendererT.begin_fill()
    #rendererT.setheading(0)
    for i in range(2):
      rendererT.forward(inventory_height - 60)
      rendererT.right(90)
      rendererT.forward(width)
      rendererT.right(90)
    rendererT.end_fill()
    rendererT.color('')
    #display the 'place' and 'craft' text
    for i in range(1,num_rows+1):
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 20 - (i * 100))
      rendererT.write("place")
      rendererT.goto(20, (height - (MAPHEIGHT * TILESIZE)) - 40 - (i * 100))
      rendererT.write("craft")
    #set the inventory position
    xPosition = 70
    yPostition = height - (MAPHEIGHT * TILESIZE) - 80
    itemNum = 0
    for i, item in enumerate(resources):
      #add the image
      rendererT.goto(xPosition, yPostition)
      rendererT.shape(textures[item])
      rendererT.stamp()
      #add the number in the inventory
      rendererT.goto(xPosition, yPostition - TILESIZE)
      rendererT.write(inventory[item])
      #add key to place
      rendererT.goto(xPosition, yPostition - TILESIZE - 20)
      rendererT.write(placekeys[item])
      #add key to craft
      if crafting.get(item) != None:
        rendererT.goto(xPosition, yPostition - TILESIZE - 40)
        rendererT.write(craftkeys[item])     
      #move along to place the next inventory item
      xPosition += 50
      itemNum += 1
      #drop down to the next row every 10 items
      if itemNum % INVWIDTH == 0:
        xPosition = 70
        itemNum = 0
        yPostition -= TILESIZE + 80
    drawing = False

#generate the instructions, including crafting rules
def generateInstructions():
  instructions.append('Crafting rules:')
  #for each resource that can be crafted...
  for rule in crafting:
    #create the crafting rule text
    craftrule = names[rule] + ' = '
    for resource, number in crafting[rule].items():
      craftrule += str(number) + ' ' + names[resource] + ' '
    #add the crafting rule to the instructions
    instructions.append(craftrule)
  #display the instructions
  yPos = height - 20
  for item in instructions:
    rendererT.goto( MAPWIDTH*TILESIZE + 40, yPos)
    rendererT.write(item)
    yPos-=20

#generate a random world
def generateRandomWorld():
  #loop through each row
  for row in range(MAPHEIGHT):
    #loop through each column in that row
    for column in range(MAPWIDTH):
      #pick a random number between 0 and 10
      randomNumber = random.randint(0,10)
      #WATER if the random number is a 1 or a 2
      if randomNumber in [1,2]:
        tile = WATER
      #GRASS if the random number is a 3 or a 4
      elif randomNumber in [3,4]:
        tile = GRASS
      #WOOD if it's a 5
      elif randomNumber == 5:
        tile = WOOD
      #SAND if it's a 6
      elif randomNumber == 6:
        tile = SAND
      #otherwise it's DIRT
      else:
        tile = DIRT
      #set the position in the tilemap to the randomly chosen tile
      world[column][row] = tile

#---
#Code starts running here
#---

#import the modules and variables needed
import turtle
import random
from variables import *
from math import ceil

TILESIZE = 20
#the number of inventory resources per row
INVWIDTH = 8
drawing = False

#create a new 'screen' object
screen = turtle.Screen()
#calculate the width and height
width = (TILESIZE * MAPWIDTH) + max(200,INVWIDTH * 50)
num_rows = int(ceil((len(resources) / INVWIDTH)))
inventory_height =  num_rows * 120 + 40
height = (TILESIZE * MAPHEIGHT) + inventory_height

screen.setup(width, height)
screen.setworldcoordinates(0,0,width,height)
screen.bgcolor(BACKGROUNDCOLOUR)
screen.listen()

#register the player image  
screen.register_shape(playerImg)
#register each of the resource images
for texture in textures.values():
  screen.register_shape(texture)
  
#create a new player object
playerT = turtle.Turtle()
playerT.hideturtle()
playerT.shape(playerImg)
playerT.penup()
playerT.speed(0)

#create another turtle to do the graphics drawing
rendererT = turtle.Turtle()
rendererT.hideturtle()
rendererT.penup()
rendererT.speed(0)
rendererT.setheading(90)

#create a world of random resources.
world = [ [DIRT for w in range(MAPHEIGHT)] for h in range(MAPWIDTH) ]

#map the keys for moving and picking up to the correct functions.
screen.onkey(moveUp, 'w')
screen.onkey(moveDown, 's')
screen.onkey(moveLeft, 'a')
screen.onkey(moveRight, 'd')
screen.onkey(pickUp, 'space')

#set up the keys for placing and crafting each resource
bindPlacingKeys()
bindCraftingKeys()

#these functions are defined above
generateRandomWorld()
drawWorld()
drawInventory()
generateInstructions()
drawPlayer()
playerT.showturtle()


