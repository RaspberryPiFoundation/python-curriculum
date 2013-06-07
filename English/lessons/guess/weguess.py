#!/usr/bin/env python
"""
This is a guess a number game for CodeClub
"""

#Import Modules
import random

def iguess():
    print '\n\n\nYou think of a whole number, between 1 and 100 inclusive'
    print 'I\'ll guess at your number, and you tell yme whether it\'s higher or lower than my guess'
    print 'Type h if your your number is higher then my guess,\nType l if it\'s lower and\nType c if I guess it correctly.'
    print '\n\nDon\'t cheat!!!\n\n'

    greaterthan = 0
    lessthan = 101

    for go in range (1, 9):
	guess = (greaterthan + lessthan)/2
	if (guess == lessthan) or (guess == greaterthan):
	  print 'So your number is greater than ',greaterthan,' and less than ', lessthan, '.'
	  print 'I\'m stumped - Are you sure you didn\'t cheat?'
	  break
	response = raw_input('Guess number '+str(go)+' is '+str(guess)+': ')
	if response == 'h':
	    greaterthan = guess
	if response == 'l':
	    lessthan = guess
	if response == 'c':
	    print 'Yeah - I love it when I\'m right!'
	    break
    else:
	print 'It\'s not fair!'         # Should never get here
        
def youguess():
    print '\n\n\nI\'m thinking of a whole number, between 1 and 100 inclusive'
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
	
print '\n\nHello.  I hope you are well today.\nLet\'s play a game of "guess my number"\n\n'
while True:
    iguess()
    youguess()
        