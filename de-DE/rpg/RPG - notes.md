---
title: RPG - Volunteer Notes
---

#Einführung:
Dieses Projekt lehrt das Spiele-Design durch durch Entwicklung eines Rollenspiel (RPG) Labyrinth-Spiels. In diesem Spiel muss der Spieler Objekte in einem Haus einsammeln und in ein spezifisches Zimmer gelangen ohne dabei von den Monstern gefunden zu werden, welche sich in manchen der Zimmer versteckt halten. Dieses Spiel wird durch die Manipulation von Wörterbüchern und Listen erstellt.

#Online Ressourcen

__Dieses Projekt benutzt Python 3.__ Wir empfehlen die Nutzung von [trinket](https://trinket.io/), um Python online zu schreiben. Dieses Projekt enthält die folgenden Trinkets:

+ ['RPG' starting point -- jumpto.cc/rpg-go](http://jumpto.cc/rpg-go)

Es gibt auch ein Trinket, welches das fertig gestellte Projekt enthält:

+ [â€˜RPGâ€™ Finished -- trinket.io/python/d06adeb527](https://trinket.io/python/d06adeb527)

#Offline Ressourcen
Dieses Projekt kann [offline beendet werden](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/), falls gewünscht. Zugang zu den Projekt-Ressourcen ist durch das Klicken auf den „Projekt-Materialien“ Link für dieses Projekt möglich. Dieser Link enthält einen Abschnitt über „Projekt-Ressourcen“, die u.a. auch Ressourcen beinhalten, welche die Kinder benötigen, um dieses Projekt offline beenden zu können. Achten Sie darauf, dass jedes Kind Zugang zu einer Kopie dieser Ressourcen hat. Dieser Abschnitt enthält die folgenden Dateien:

+ rpg/rpg.py

Sie finden ein fertig gestelltes Projekt in dem Abschnitt 'Volunteer Resources' (Helfer-Ressourcen), der u.a. auch Folgendes enthält:

+ rpg-finished/rpg.py

(Alle der o.g. Ressourcen können auch als Projekt und Helfer `.zip` Dateien heruntergeladen werden.)

#Lernziele
+ Spiel-Design;
+ Bearbeitung:
	+ Listen;
	+ Wörterbücher.
+ Boolesche Ausdrücke.

Dieses Projekt deckt Elemente aus den folgenden Bereichen des [Raspberry Pi Lehrplans zur digitalen Produktion](http://rpf.io/curriculum):

+ [Kombiniere die Programmierungskonstrukte, um ein Problem zu lösen.](https://www.raspberrypi.org/curriculum/programming/builder)

#Aufgaben
+ Neue Zimmer hinzufügen;
+ Gegenstände zum Einsammeln hinzufügen;
+ Feinde (Monster), die es zu vermeiden gilt, hinzufügen;
+ Entwickele dein eigenes Spiel.

#Häufig gestellte Fragen (FAQ)
+ Die Kinder müssen evtl. daran erinnert werden, dass die Elemente in einem Wörterbuch, bzw. in einer Liste durch ein Komma getrennt werden. Zum Beispiel: Wenn ein neues Zimmer zum 'rooms' (Zimmer) Wörterbuch hinzugefügt wird, muss ein Komma zwischen dem neu hinzugefügten Zimmer und dem bereits vorhandenen Zimmer gesetzt werden.
+ Wenn ein neues Zimmer hinzugefügt wird, könnten die Kinder u. U. vergessen, einen Link zwischen einem vorhandenen Zimmer und einem neu geschaffenen Zimmer hinzuzufügen. Das würde bedeuten, dass die Kinder zwar ein Zimmer verlassen, es aber nicht betreten können!
+ Der Code zur Überprüfung, ob der Spieler das Spiel gewonnen oder verloren hat, muss eingerückt werden, um zu gewährleisten, dass diese Überprüfung bei Betreten eines jeden neuen Zimmers ausgeführt wird. Wenn der Code nicht eingerückt ist, dann liegt er außerhalb der Hauptspielschlaufe und läuft niemals.

