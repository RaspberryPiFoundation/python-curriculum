---
title: Tajne poruke — Bilješke za voditelje Kluba
language: hr-HR
embeds: "*.png"
...

#Uvod:
U ovom projektu djeca će naučiti kako napraviti vlastiti program za šifriranje poruka te poslati i primiti šifriranu poruku od prijatelja. Vrši se ponavljanje (korištenjem petlji) nad tekstualnim nizom.

#Online izvori

__U ovom projektu koristi se Python 3.__ Predlažemo korištenje [trinketa](https://trinket.io/) za online pisanje u Pythonu. Ovaj projekt sadrži sljedeće Trinkete:

+ [Novi (prazni) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Također je uključen i trinket koji sadrži dovršen projekt:

+ [‘Secret Messages’ dovršeni projekt -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ [‘Friendship Calculator’ dovršeni projekt -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

#Offline izvori
Ako želite, ovaj projekt možete [izraditi offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/).

Dovršenu verziju projekta možete pronaći i u odjeljku 'Volunteer Resources' koji sadrži i:

+ messages-finished/messages.py
+ messages-finished/friends.py

(Svi spomenuti materijali nalaze se u materijalima projekta i materijalima za volontere, koje je moguće preuzeti kao `.zip` datoteke.)

#Ishodi učenja
+ Ponavljanje (korištenjem petlji) nad varijablom tipa string;
+ Korištenje naredbe `find()`;
+ Modularni operator (`%`).

#Izazovi
+ Koristi Cezarovu šifru - šifriranje i dešifriranje slova i riječi ručno;
+ Promjenjivi ključevi - omogućuje korisniku unos željenog ključa;
+ Šifriranje i dešifriranje poruka - šifriranje i dešifriranje cijelih poruka;
+ Kalkulator prijateljstva - primjena ponavljanja teksta na novom problemu.

#Često postavljana pitanja
+ Kod pretraživanja pomoću naredbi `find()` ili `if char in alphabet:` ne zaboravite da su naredbe osjetljive na velika i mala slova. Djeca mogu koristiti:

	```python
	message = input("Unesite poruku koju zelite sifrirati: ").lower()
	```

	da unos bude ispisan malim slovima prije pretraživanja.
