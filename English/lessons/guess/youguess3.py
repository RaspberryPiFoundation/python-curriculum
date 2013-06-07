#!/usr/bin/env python
"""
This is a guess a number game for CodeClub
"""

#Import Modules
import random

print '\n\nHello.  I hope you are well today.\nLet\'s play a game of "guess my number"\n\n'
print 'I\'m thinking of a whole number, between 1 and 100 inclusive'
print 'I\'ll give you 8 goes at guessing it, and tell you whether it\'s higher or lower than your guess'
print '(I\'m feeling generous, you should only need 7 goes ;-) )'

correct = random.randint(1,100)
#print 'Don\'t tell anybody, but I\'m thinking of the number ', correct

for go in range (1, 9):
    guess = input('Guess number '+str(go)+':')
    if guess < correct:
	print 'It\'s bigger than', guess
    if guess > correct:
	print 'It\'s smaller than', guess
    if guess == correct:
	print 'Correct!  Brilliant, you are so clever!'
	break
else:
    print 'That\'s all your goes, and you didn\'t guess it - I win!'
        


        