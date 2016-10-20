#lista liter do szyfrowania
alfabet = "abcdefghijklmnopqrstuvwxyz"

#tajny klucz to 3
klucz = 3

litera = input("Wprowadz litere do zaszyfrowania: ")

#znajdz pozycje litery w alfabecie
#na przyklad 'a' jest na pozycji 0, 'e' jest na pozycji 4, itd.
pozycja = alfabet.find(litera)

#dodaj tajny klucz aby otrzymac pozycje zaszyfrowanej litery
# % 26 oznacza 'wroc do 0 kiedy osiagniesz 26'
nowaPozycja = (pozycja + klucz) % 26

#zaszyfrowana litera znajduje sie na pozycji nowaPozycja w alfabecie
zaszyfrowanaLitera = alfabet[nowaPozycja]
        
print("Twoja litera po zaszyfrowaniu to" , zaszyfrowanaLitera)