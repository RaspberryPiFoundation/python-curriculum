#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = 'Favourite Pet'
piechart.add('Dog', 6)
piechart.add('Cat', 4)
piechart.add('Hamster', 3)
piechart.add('Fish', 2)
piechart.add('Snake', 1)
piechart.render()

barchart = pygal.Bar()
barchart.title = 'Favourite Pet'
barchart.add('Dog', 6)
barchart.add('Cat', 4)
barchart.add('Hamster', 3)
barchart.add('Fish', 2)
barchart.add('Snake', 1)
barchart.render()
  
piechart2 = pygal.Pie()
barchart2 = pygal.Bar()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))
    barchart2.add(label, int(value))
    
file.close()

#piechart2.render()
#barchart2.render()

butterflies = pygal.Bar()
butterflies.title = 'Butterfly Count'

file = open('butterflies.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(': ')
    butterflies.add(label, int(value))
file.close()

butterflies.render()

pn = pygal.Bar()
pn.title = 'Pirates vs Ninjas'

file = open('piratesninjas.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    pn.add(label, int(value))
file.close()

pn.render()
