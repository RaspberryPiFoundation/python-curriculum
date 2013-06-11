#!/usr/bin/env python
"""
This is a guess a number game for CodeClub
"""

print '\n\nHello.  I hope you are well today.\nLet\'s play a game of "guess my number"\n\n'
print 'You think of a whole number, between 1 and 100 inclusive'
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
        


        