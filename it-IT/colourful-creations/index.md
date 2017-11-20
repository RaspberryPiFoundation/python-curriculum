---
title: Creazioni colorate
description: Crea i tuoi colori personalizzati e usali per creare un coloratissimo poster. 
notes: "Colourful Creations - notes.md"
layout: project
new: true
---

# Introduzione {.intro}

In questo progetto creerai un dizionario di colori che mappa i codici dei colori (difficilissimi da ricordare) con dei nomi più descrittivi.  

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/41a99e668b?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/colourful-finished.png">
</div>

# Passo 1: Come usare i codici esadecimali dei colori { .activity}

## Lista di controllo delle attività { .check}

La "tartaruga" di Python contiene già dei colori predefiniti ("red" per rosso, "white" per bianco, ecc.) ma puoi utilizzare anche i codici esadecimali dei colori (che forse hai già visto nel corso di HTML e CSS). 

+ Apri il modello vuoto di Python Trinket: <a href="http://jumpto.cc/python-new" target="_blank">jumpto.cc/python-new</a>. 

+ Aggiungi il seguente codice di impostazione per utilizzare la tartaruga:

    ![screenshot](images/colourful-setup.png)
    
    Nota che hai usato un colore con un nome già assegnato: "white", il bianco.
    
+ Tartaruga contiene già un elenco di nomi di colori che puoi usare, ma alle volte potresti voler scegliere dei colori personali. Tartaruga ti consente di usare i codici esadecimali dei colori. 

  Apri <a href="http://jumpto.cc/colour-picker" target="_blank">jumpto.cc/colour-picker</a> e scegli un colore che ti piace. Trova il suo codice esadecimale, che comincia con "#", ad esempio "#A7E30E". 
  
+ Copia il codice esadecimale, compreso il cancelletto, evidenziandolo, premendo il tasto destro del mouse, e quindi scegliendo Copia, oppure premendo Ctrl-C. 
  
+ Adesso cambia la linea di codice che imposta il colore dello schermo, per usare il colore che hai scelto. Ad esempio:

   ![screenshot](images/colourful-background.png)
   
   Per incollare il tuo codice esadecimale in Trinket puoi premere il tasto destro del mouse e scegliere Incolla, oppure puoi premere Ctrl-V. 
  
+ Scegli un altro codice esadecimale di colore e usalo per creare del testo colorato:

   ![screenshot](images/colourful-write.png)
   
   Non sei obbligato a usare il font "Arial". Puoi scegliere "Verdana", "Times" o "Courier".
   
   "40" indica le dimensioni del font. Se vuoi puoi cambiare anche questo.  
   
+ Prova a usare colori diversi fino a trovare i due colori che stanno davvero meglio insieme. 


## Salva il progetto {.save}

# Passo 2: Un dizionario di colori{ .activity}

## Lista di controllo delle attività { .check}
 
I codici esadecimali dei colori sono molto utili, ma sono difficili da ricordare. 

Come certamente sai, un dizionario ti consente di cercare una parola e vedere cosa vuol dire. In Python, un dizionario è persino più potente. Ti permette di cercare un valore per ogni "chiave" contenuta nel dizionario.

Creiamo adesso un dizionario per mappare la corrispondenza fra i normali nomi dei colori che capiscono le persone (chiavi) e il codici esadecimali (valori) che capiscono i computer.

+ I dizionari sono contenuti fra parentesi graffe. 

  Crea un dizionario vuoto chiamato "colours" (colori):

   ![screenshot](images/colourful-dict.png)
   
+ Scegli dei nomi carinissimi per i tuoi colori e modifica la riga "colours = {}" per aggiungere le corrispondenti voci al dizionario. 

  Questo è un esempio di dizionario di colori:

   ![screenshot](images/colourful-colours.png)
   
   I due punti (:) separano la chiave (nome del colore) dal valore (codice esadecimale). Nel dizionario, ogni coppia chiave:valore deve essere separata dalle altre con una virgola (,). 

+ Adesso non è più necessario ricordare i codici esadecimali: puoi semplicemente cercarli nel dizionario. 

  Adatta il seguente codice per usare i tuoi nomi di colori:
  
  ![screenshot](images/colourful-entries.png)
  
  La chiave va fra le parentesi quadre "[]" dopo il nome del dizionario. 
  
+ Adesso puoi aggiornare il codice per fargli cercare i colori nel dizionario.

  ![screenshot](images/colourful-use.png)
  
  
+ Prova il codice per controllare che il testo venga visualizzato ancora correttamente. 

## Salva il progetto {.save}

## Sfida: Altri colori! {.challenge}

Puoi aggiungere altri colori al dizionario e provarli? Usa <a href="http://jumpto.cc/colour-picker" target="_blank">jumpto.cc/colour-picker</a> per trovare altri colori. 

Non dimenticare di darei ai tuoi colori dei nomi impressionanti! 

Ecco un esempio di codice per ricordarti come usare la tartaruga:

![screenshot](images/colourful-challenge1.png)


## Salva il progetto {.save}

## Sfida: Crea un poster

Gli artisti e i designer spesso creano una "tavolozza" di colori che vanno bene insieme per un tema particolare come ad esempio il deserto oppure lo spazio. 

Puoi creare un nuovo progetto di Python che utilizza un dizionario per una tavolozza di colori a tema. Puoi scegliere l'autunno, il bosco, il mare, il Natale, i gelati, i colori della tua squadra preferita o qualsiasi altra idea preferisci. 

Crea un poster con il dizionario della tua tavolozza di colori.

Puoi usare tutti i comandi di tartaruga che conosci, come ad esempio "forward", "right", "left", "penup" e "pendown". 

E cosa ne dici di aggiungere anche una cornice al tuo poster?

Altri utili comandi tartaruga:

+ "circle(50)" disegna il bordo di un circolo con raggio 50.
+ "dot(100)" disegna un circolo di colore pieno con diametro 100. 
  
Ecco un esempio:

![screenshot](images/colourful-finished.png)

## Salva il progetto {.save}


