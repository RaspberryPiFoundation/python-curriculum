---
title: Secret Messages - Volunteer Notes
---

#Einführung:
In diesem Projekt lernen die Kinder, wie man ein Verschlüsselungsprogramm erstellt, um geheime Mitteilungen mit einem Freund austauschen zu können (schicken und empfangen). Dieses Projekt bietet eine Einführung in die Iteration (Schleife) über eine Textfolge.

#Online Ressourcen

__Dieses Projekt benutzt Python 3.__ Wir empfehlen die Nutzung von [trinket](https://trinket.io/), um Python online zu schreiben. Dieses Projekt enthält die folgenden Trinkets:

+ [Neues (leeres) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

Es gibt auch ein Trinket, welches das fertig gestellte Projekt enthält:

+ [â€˜Secret Messagesâ€™ Finished -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ [â€˜Friendship Calculatorâ€™ Finished -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

#Offline Ressourcen
Dieses Projekt kann [offline beendet werden](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) , falls gewünscht.

Sie können das fertig gestellte Projekt im Abschnitt „Helfer-Ressourcen“ finden, der u.a. auch Folgendes enthält:

+ messages-finished/messages.py
+ messages-finished/friends.py

(Alle der o.g. Ressourcen können auch als Projekt und Helfer `.zip` Dateien heruntergeladen werden.)

#Lernziele
+ Iteration (Schleife) über eine Zeichenfolge-Variable;
+ Die `find()` (finden) Methode;
+ Der Modulo-Operator (`%`).

Dieses Projekt deckt Elemente aus den folgenden Bereichen des [Raspberry Pi Lehrplans zur digitalen Produktion](http://rpf.io/curriculum):

+ [Kombiniere die Programmierkonstrukte, um ein Problem zu lösen.](https://www.raspberrypi.org/curriculum/programming/builder)

#Aufgaben
+ Benutze eine Caesar-Schiffre: Briefe und Worte manuell verschlüsseln und entschlüsseln;
+ Variable Keys: Sie ermöglichen dem Nutzer einen spezifischen Key einzugeben;
+ Mitteilungen verschlüsseln und entschlüsseln: Die Ver- und Entschlüsselung von kompletten Mitteilungen;
+ Freundschaftsrechner: Die Text-Iteration bei einem neuen Problem anwenden.

#Häufig gestellte Fragen (FAQ)
+ Wenn mit Hilfe von `find()` (finden) gesucht wird, bzw. `if char in alphabet:` (wenn das Zeichen im Alphabet ist) beachten Sie bei der Suche bitte die Groß- und Kleinschreibung. Die Kinder können Folgendes benutzen:

	```python
	message = input("Bitte eine Meldung zum Verschlüsseln eingeben: ").lower()
	```

	damit die Eingabe vor der etwaigen Suche in Kleinschrift erfolgt.
