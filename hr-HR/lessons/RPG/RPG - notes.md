---
title: RPG — Bilješke za voditelje Kluba
language: hr-HR
embeds: "*.png"
...

#Uvod:
U ovom projektu djeca uče o dizajnu igara kroz izradu RPG igre labirinta. U ovoj igri igrač mora sakupiti objekte unutar kuće i doći do određene prostorije, a pritom izbjegavati čudovišta koja vrebaju u nekim prostorijama. Igra će biti napravljena manipuliranjem rječnicima i listama.

#Online izvori

__U ovom projektu koristi se Python 3.__ Predlažemo korištenje [trinketa](https://trinket.io/) za online pisanje u Pythonu. Ovaj projekt sadrži sljedeće Trinkete:

+ ['RPG' početni materijal -- jumpto.cc/rpg-go](http://jumpto.cc/rpg-go)

Također je uključen i trinket koji sadrži dovršen projekt:

+ [‘RPG’ dovršeni projekt -- trinket.io/python/d06adeb527](https://trinket.io/python/d06adeb527)

#Offline izvori
Ako želite, ovaj projekt možete [izraditi offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/). Materijalima projekta možete pristupiti klikom na poveznicu 'Project Materials'. Poveznica sadrži odjeljak 'Project Resources' u kojem se nalaze materijali koji će djeci biti potrebni za izradu projekta offline. Pobrinite se da svako dijete ima pristup kopiji ovih materijala. U odjeljku se nalaze sljedeće datoteke:

+ rpg/rpg.py

Dovršenu verziju projekta možete pronaći i u odjeljku 'Volunteer Resources' koji sadrži i:

+ rpg-finished/rpg.py

(Svi spomenuti materijali nalaze se u materijalima projekta i materijalima za volontere, koje je moguće preuzeti kao `.zip` datoteke.)

#Ishodi učenja
+ Dizajn igara;
+ Uređivanje:
	+ Lista;
	+ Rječnika;
+ Booleovi izrazi.

#Izazovi
+ Dodavanje novih prostorija;
+ Dodavanje predmeta za sakupljanje;
+ Dodavanje neprijatelja za izbjegavanje;
+ Osmisli vlastitu igru.

#Često postavljana pitanja
+ Djecu će možda biti potrebno podsjetiti da se elementi u rječniku/listi odvajaju zarezom. Primjerice, kada dodajemo novu prostoriju u rječnik 'rooms', između nove prostorije i zadnje prostorije koja se nalazi u rječniku moramo dodati zarez.
+ Pri dodavanju nove prostorije, djeca će možda zaboraviti u novoj prostoriji dodati poveznicu na već postojeću sobu. To znači da će moći izaći iz prostorije, ali ne i ući u nju!
+ Dio kôda koji provjerava je li igrač pobjedio ili izgubio u igri mora biti uvučen kako bi se osiguralo da se ta provjera obavlja prilikom svakog ulaska u novu prostoriju. Ukoliko kôd nije uvučen, onda će se nalaziti izvan glavne petlje igre i neće se nikada pokrenuti.
