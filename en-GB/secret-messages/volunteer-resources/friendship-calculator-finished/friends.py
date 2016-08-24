#!/bin/python3

score = 0
names = input('enter tha names of 2 people: ')

for character in names:
  if character in 'aeiou':
    score += 5
  if character in 'friend':
    score += 10

print('your friendship score is :', score)

if score > 100:
  print('best friends!')