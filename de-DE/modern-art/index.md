---
title: Moderne Kunst
description: Programmiere deine eigeneModerne Kunst, die per Computer erzeugt wird. 
notes: "Modern Art - notes.md"
layout: project
new: true
---

# Einführung { .intro}

In diesem Projekt wirst du Moderne Kunst per Computer erzeugen. Du wirst Funktionen benutzen, um ein Programm zu schreiben, das du danach immer wieder benutzen kannst. 
 
<div class="trinket">
  <iframe src="https://trinket.io/embed/python/47bbc2fc2b?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/modern-finished.png">
</div>

# Schritt 1: Zufällig ausgesuchte Farben { .activity}

## Aufgaben-Checkliste { .check}

+ Dieses Trinket öffnen: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>. 

+ Du kannst die Farbe einer Schildkröte bestimmen, indem du festlegst, wie viel rot, grün und blau du von 0 bis 255 auswählst. 

    Füge den folgenden Code hinzu, um eine lila Schildkröte zu erhalten:

    ![screenshot](images/modern-purple.png)
   
    Lila wird aus der Mischung von zwei Farben, nämlich rot und blau, hergestellt.

+ Probiere mal ein paar verschiedene Ziffern aus, um unterschiedliche Farben zu erhalten. 

    Bitte denk daran, jede Ziffer kann von 0 bis 255 gehen. 

+ Wie wäre es, wenn du eine Farbe einfach zufällig aussuchst?

    Aktualisiere deinen Code und wähle eine zufällig ausgesuchte Ziffer zwischen 0 und 255 für die Werte von rot, grün und blau:
    
    ![screenshot](images/modern-random-colour.png)

+ Klicke ein paar Mal auf â€˜Runâ€™ (laufen lassen), um unterschiedlich gefärbte Schildkröten zu erhalten.

+ Das ist zwar toll, aber man muss sich hierbei jedoch unheimlich viel merken und dies jedes Mal neu eintippen, wenn man die Schildkröte zu einer zufällig ausgesuchten Farbe einstellen will. Außerdem ist es schwer zu lesen. 

    In Python können wir `def` (definieren) schreiben, um eine Funktion zu  definieren, die wir aufrufen können, wannimmer wir die Schildkröte zu einer zufällig ausgesuchten Farbe einstellen wollen. 

    Du hast bereits schon Funktionen aufgerufen: `color()` (Farbe) und `randint()` sind Funktionen, die für dich definiert worden sind. 

    Lass uns den zufällig ausgesuchten Farbcode in eine Funktion eingeben mit Hilfe von def (definieren):
  
    ![screenshot](images/modern-colour-function.png)
    
  Achte darauf, dass du den Code innerhalb der Funktion einrückst. Funktionen werden normalerweise über dem Script nach den Importen platziert. 
  
+ Wenn du jetzt auf deinen Code â€˜Runâ€™ (laufen lassen) klickst, wirst du nun keine zufällig ausgesuchte Farbe für deine Schildkröte erhalten. Das liegt daran, dass due deine Funktion zwar definiert hast, du hast sie aber noch nicht aufgerufen. 
  
+ Füge eine neue Zeile hinzu, um deine Funktion aufzurufen:
  
    ![screenshot](images/modern-call-colour.png)

    Siehst du jetzt, dass der neue Code viel leichter zu verstehen ist, weil der komplexe Teil die Funktionen sind? Es ist einfach herauszufinden, was `randomcolour()` (zufällig ausgesuchte Farbe) macht.

# Schritt 2: Zufällig ausgesuchter Ort { .activity}

## Aufgaben-Checkliste { .check}

Lass uns eine weitere Funktion herstellen, um die Schildkröte zu einem beliebigen Platz auf dem Bildschirm zu bewegen. Die Mitte des Bildschirms ist (0,0), wir müssen die Schildkröte daher in einen quadratischen Bereich rund um die Mitte setzen. 

+ Füge eine `randomplace()` (zufällig ausgesuchter Ort) Funktion hinzu:

    ![screenshot](images/modern-place-function.png)
    
+ Probiere deine neue Funktion aus, indem du sie aufrufst und rufe dann `stamp()` (stempeln) auf, du kannst es mehr als einmal aufrufen:

    ![screenshot](images/modern-call-place.png)

+ Ach herrje! Die Schildkröte zieht, wenn sie sich bewegt. Lass uns den Stift am Anfang hoch- und am Ende runternehmen, damit die Schildkröte nicht zieht während sie sich bewegt:

    ![screenshot](images/modern-place-pen.png)
    
    Hast du gemerkt, dass du den Code nur an einem Platz 'fix' (beheben) musstest? Das ist der Vorteil an den Funktionen. 

+ Teste jetzt deinen Code ein paar Mal.

## Projekt speichern {.save}

## Aufgabe: Schildkröten-Kunst {.challenge}
Kannst du eine Funktion `randomheading()` (zufällige Richtung) definieren, wodurch die Schildkröte sich in eine zufällige Richtung bewegt und kannst du es schaffen, dass der folgende Code funktioniert?

![screenshot](images/modern-turtle-art.png)

Tipps:

- `setheading(<number>)` (Richtung einstellen (Zahl)) ändert die Richtung, in welche die Schildkröte geht.

- `<number>`  (Die Zahl) sollte zwischen 1 und 360 liegen (der Gradanzahl in einem Kreis)

- Du kannst `randint(1, 360)` benutzen, um eine Zahl zwischen 1 und 360 zu wählen.

## Projekt speichern {.save}

# Schritt 3: Ein Rechteck in Moderner Kunst erstellen { .activity}

## Aufgaben-Checkliste { .check}

Lass uns jetzt Moderne Kunst produzieren, indem wir ganz viele Rechtecke in verschiedenen Größen und Farben zeichnen. 

+ Addiere als erstes den folgenden Code zum unteren Teil deines Scripts, nach dem Aufgaben-Code, um den Bildschirm nach deiner Schildkröten-Kunst zu leeren und um die Schildkröte wieder in die normale Richtung zu weisen:

    ![screenshot](images/modern-reset.png)

+ Du kannst deinen Code für das Schildkrötenbild wegkommentieren, indem du ein `#` Rautenzeichen zu Beginner jeder Zeile setzt, damit es nicht läuft, während du an dem Rechteck-Bild arbeitest. (Du kannst diesen Kommentar später wieder entfernen, um dein Gesamtkunstwerk zu zeigen.)

    ![screenshot](images/modern-comment.png)
 
+ Lass uns jetzt eine Funktion hinzufügen, um ein beliebig großes Rechteck mit einer zufällig ausgesuchten Farbe an einem zufällig ausgesuchten Platz zu zeichnen! 
    
    Füge die `drawrectangle()` (Rechteck zeichnen) Funktion nach deinen anderen Funktionen hinzu:

    ![screenshot](images/modern-rect-function.png)
    
    Schau mal unter `snippets.py`, um einen Helfer-Code zu finden, wenn du dir zusätzliche Zeit beim Eintippen ersparen willst. 
    
+ Füge den folgenden Code zum unteren Teil von `main.py`, um deine neue Funktion aufzurufen:

    ![screenshot](images/modern-call-rect.png)
    
    Lass dein Script ein paar Mal laufen, um zu sehen, wie sich die Höhe und Breite verändert. 
   
+ Das Rechteck hat immer die gleiche Farbe und beginnt am gleichen Ort. 

    Jetzt musst du die Schildkröte in einer zufällig ausgesuchten Farbe einstellen und sie dann zu einem zufällig ausgesuchten Platz bewegen. He! Hattest du nicht hierfür bereits schon Funktionen angefertigt? Super. Du kannst diese einfach vom Beginn der Rechteck Funktion aufrufen: 
    
    ![screenshot](images/modern-random-rect.png)
    
    Wow! Das war wesentlich weniger Arbeit und es ist viel leichter zu lesen. 

    
+ Lass uns jetzt die Funktion `drawrectangle()` (Rechteck zeichnen) in einer Schleife aufrufen, um coole Moderne Kunst zu produzieren:

    ![screenshot](images/modern-rect-art.png)

+ Ach herrje! Das hat jetzt aber eine Weile gedauert, nicht wahr?! Glücklicherweise kannst du die Schildkröte schneller laufen lassen. 

    Finde die Linie, in der die Form auf 'turtle' (Schildkröte) einstellst und füge dann den markierten Code hinzu:
    
    ![screenshot](images/modern-speed.png)
    
    `speed(0)` (Geschwindigkeit 0) ist der Schnellste oder du kannst die Zahlen von 1 (langsam) bis 10 (schnell) benutzen. Experimente hiermit ein wenig, bis du deine gewünschte Geschwindigkeit gefunden hast. 

## Aufgabe: Noch mehr Moderne Kunst { .challenge}
Kannst du eine Funktion kreieren, die eine Form zeichnet und dann entweder deine Funktionen `randomcolour()` (zufällige Farbe), bzw. `randomplace()` (zufälliger Ort) aufruft? 

Du kannst deine Funktion innerhalb einer `for` (für) Schleife aufrufen, wie du es bereits beim Rechteck-Bild gemacht hast, um die Moderne Kunst zu schaffen. 

Ideen:

- Schildkröten haben eine Funktion, die sich “dot” nennt, hierdurch wird ein Radius (die Entfernung von der Mitte bis zum Rand esines Kreises) als Eingabefaktor genommen. Z. B. turtle.dot(10) (Schildkröte.dot (10)). Du kannst eine `drawcircle()` (Kreis zeichnen) Funktion erstellen, die einen Kreis mit einem zufälligen Radius zeichnet. 
    
    ![screenshot](images/modern-circles.png)
    
- Schau mal unter `snippets.py` für einen Muster-Code, um mit der Schildkröte Sterne zu zeichnen.
    
    ![screenshot](images/modern-stars.png) 


## Projekt speichern {.save}

