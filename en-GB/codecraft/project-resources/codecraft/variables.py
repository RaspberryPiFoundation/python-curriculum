#!/bin/python3

#Game variables that can be changed!

#game background colour.
BACKGROUNDCOLOUR = 'white'

#map variables.
MAXTILES  = 20
MAPWIDTH  = 10
MAPHEIGHT = 10

#variables representing the different resources.
DIRT    = 0
GRASS   = 1
WATER   = 2
BRICK   = 3

#a list of all game resources.
resources = [DIRT,GRASS,WATER,BRICK]

#the names of the resources.
names = {
  DIRT    : 'dirt',
  GRASS   : 'grass',
  WATER   : 'water',
  BRICK   : 'brick'
}

#a dictionary linking resources to images.
textures = {
  DIRT    : 'dirt.png',
  GRASS   : 'grass.png',
  WATER   : 'water.png',
  BRICK   : 'brick.png'
}

#the number of each resource the player has.
inventory = {
  DIRT    : 10,
  GRASS   : 10,
  WATER   : 10,
  BRICK   : 0
}

#the player image.
playerImg = 'player.png'

#the player position.
playerX = 0
playerY = 0

#rules to make new resources.
crafting = {
  BRICK    : { WATER : 1, DIRT : 2 }
}

#keys for placing resources.
placekeys = {
  DIRT  : '1',
  GRASS : '2',
  WATER : '3',
  BRICK : '4'
}

#keys for crafting tiles.
craftkeys = {
  BRICK : 'r'
}

#game instructions that are displayed.
instructions =  [
  'Instructions:',
  'Use WASD to move'
]
