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
print 'Don\'t tell anybody, but I\'m thinking of the number ', correct

        


        