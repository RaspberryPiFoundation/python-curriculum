from random import *

#print the 3 doors and the game instructions
print('''
Gameshow!
=========

There's a prize behind one of the 3 doors!
Guess the correct door to win the prize!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|

Choose a door (1, 2 or 3):
''')

#get the chosen door and store it as an integer (whole number)
chosenDoor = input()
chosenDoor = int(chosenDoor)

#randomly choose the winning door number (between 1 and 3)
winningDoor = randint(1,3)

#show the player the winning and chosen door numbers
print("The chosen door is", chosenDoor)
print("The winning door is", winningDoor)

#player wins if the chosen door and winning door number are the same
if chosenDoor == winningDoor:
    print("Well done!")
else:
    print("Unlucky!")
