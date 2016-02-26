print('''
P1 - "W Pythonie, jak nazywa siê 'pude³ko' w którym trzymamy dane?
a - tekst
b - zmienna
c - pude³ko na buty
''')
odpowiedz = input().lower()

if odpowiedz == "a":
    print(" Niestety - tekst to typ danych :( ")
elif odpowiedz == "b":
    print(" Zgadza sie!! :) ")
elif odpowiedz == "c":
    print(" Chyba siê wyg³upiasz... :( ")
else:
    print(" Nie wybra³aœ/wybra³eœ a, b or c :( ")

