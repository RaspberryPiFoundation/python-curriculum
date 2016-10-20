from random import *

#gracz zmienia ta zmienna zeby zakonczyc gre
gramDalej = True

punkty = 0

#wyswietl instrukcje gry
print('''
Dwadziescia jeden!
==================
Sproboj zebrac dokladnie 21 punktow
''')

#powtarzaj tak dlugo jak zmienna gramDalej jest uswationwa na True
while gramDalej == True:

    #losowo wybierz liczbe od 1 do 10
    nowaLiczba = randint(1,10)

    #dodaj nowa liczbe do punktow
    punkty = punkty + nowaLiczba

    #wyswiell nowe dane 
    print("\nTwoja nowa liczba to ", nowaLiczba)
    print("Twoja obecna liczba puntkow to", punkty)

    #zakoncz gre jesli gracz odpowie 'n'
    #lub jesli liczba punktow jest wieksza od 21
    print("\nCzy chcesz dodac kolejna liczbe? (t/n)")
    odpowiedz = input()
    if odpowiedz.lower() == 'n' or punkty > 21:
        gramDalej = False
    
print("\nTwoja koncowa liczba punktow to", punkty)

#gracz zwycieza jesli punkty wynosza 21
if punkty == 21:
    print("WYGRALES!!")
else:
    print("Niestety, przegrales!")
