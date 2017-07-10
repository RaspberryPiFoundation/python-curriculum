#!/bin/python3

print('Bonjour, je peux programmer en Python!')

print('''
Mon animal favori est le mouton

 o-###-
   | |   #

J'habite à Montréal

        #
       ###       _|_
  __----#__    _|   |_
--      #  --_| |   | |
              | |   | |
              | |   | |

''')

naissance = input('En quelle année es-tu né(e)?')
naissance = int(naissance)
age = 2025 - naissance
print('En l\'an 2025, tu auras', age, 'ans')
