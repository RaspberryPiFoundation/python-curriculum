from random import *

#wyswietl 3 drzwi i zasady gry
print('''
Teleturniej!
=========

Za jednymi z tych drzwi znajduje siê nagroda!
Wybierz te w³aœciwe i zgarnij nagrodê!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

punkty = 0

#daj graczowi 3 szanse
for szansa in range(3):

    print("\nWybierz drzwi (1, 2 or 3):")

    #wczytaj wybrane drzwi i zapisz je jako liczbe calkowita
    wybraneDrzwi = input()
    wybraneDrzwi = int(wybraneDrzwi)

    #losowo wybierz liczbe oznaczajaca zwycieskie drzwi (liczbe pomiedzy 1 a 3)
    drzwiZNagroda = randint(1,3)

    #wyswietl graczowi wybrane i zwycieskie drzwi
    print("Wybrales drzwi numer", wybraneDrzwi)
    print("Wygrywaja drzwi numer", drzwiZNagroda)

    #gracz wygrywa, jesli wybrane drzwi i wygrywajace drzwi sa takie same
    if wybraneDrzwi == drzwiZNagroda:
        print("Gratulacje!")
        punkty = punkty + 1
    else:
        print("Niestety, przegrales!")

    print("Twoja liczba punktow to", punkty)

print("Twoja koncowa liczba punktow to", punkty)