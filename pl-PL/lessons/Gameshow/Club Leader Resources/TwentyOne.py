from random import *

#the user changes this varialbe to end the game
playing = True

score = 0

#print the game instructions
print('''
Twenty One!
===========
Try to score exactly 21 points!
''')

#repeat as long as the 'playing' variable is set to 'True'
while playing == True:

    #randomly choose a number between 1 and 10
    newNumber = randint(1,10)

    #add the new number to the score
    score = score + newNumber

    #show the data to the player
    print("\nYour next number is", newNumber)
    print("Your score is now", score)

    #end the game if the user types 'n'
    #or if the score is over 21
    print("\nDo you want to add another number? (y/n)")
    answer = input()
    if answer.lower() == 'n' or score > 21:
        playing = False
    
print("\nYour final score is", score)

#the player wins if they score 21
if score == 21:
    print("YOU WIN!!")
else:
    print("Unlucky!")
