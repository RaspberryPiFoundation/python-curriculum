---
title: CodeCraft
description: Miglioramenti al design e al codice di una versione 2D di Minecraft.
notes: "CodeCraft - notes.md"
layout: project
---

# Introduzione {.intro}

In questo progetto apporterai miglioramenti al design e al codice di una versione 2D di Minecraft.

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/9ac3995d69?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/craft-finished.png">
</div>

# Passo 1: Il gioco { .activity}

## Lista di controllo delle attività { .check}

+ Apri questo trinket: <a href="http://jumpto.cc/codecraft-go" target="_blank">jumpto.cc/codecraft-go</a>. 

+ Usa i tasti WASD della tastiera per spostare il giocatore nel mondo, che è pieno di tante risorse diverse (terra, erba e acqua).

    ![screenshot](images/craft-move.png)

+ Premi la barra spaziatrice per raccogliere risorse. Raccogli qualche risorsa diversa e vedi come vengono aggiunte al tuo inventario.

    ![screenshot](images/craft-pickup.png)

+ Premi i tasti numerici (da 1 a 3) per collocare una risorsa sulla mappa. Ad esempio, premi 3 per mettere un po' d'acqua sulla mappa. Questo funzionerà solo se hai dell' acqua nell'inventario.

    ![screenshot](images/craft-place-water.png)

+ Puoi fabbricare un oggetto premendo il tasto visualizzato nel menu. Fabbricare significa combinare insieme elementi che hai già nell'inventario per crearne di nuovi. Prova a premere il tasto "r" per fabbricare un nuovo mattone (purché tu abbia 2 terre e 1 acqua nell'inventario).

    ![screenshot](images/craft-craft-brick.png)

+ Dopodiché puoi premere il tasto "4" per collocare i mattoni che hai fabbricato.

    ![screenshot](images/craft-place-brick.png)

## Salva il progetto {.save}

## Sfida: Costruisci il tuo mondo {.challenge}
Sei capace a costruire una casetta con giardino e piscina? Cos'altro puoi creare?

![screenshot](images/craft-build-example.png)

## Salva il progetto {.save}

# Passo 2: Personalizzazione del gioco { .activity}

Modifichiamo adesso qualche variabile per vedere come funziona il gioco.

+ Fai clic sul file "variables.py" per vedere delle variabili che possono essere modificate.

    ![screenshot](images/craft-variables.png)

+ Modifica il valore della variabile "BACKGROUNDCOLOUR" e fai clic su "Run" per vedere in che modo cambia il gioco.

    ![screenshot](images/craft-background.png)

+ La variabile "MAXTILES" indica la quantità di ciascuna risorsa che può essere tenuta nell'inventario. Modifica questa variabile per poter conservare più (o meno) di 20 unità di ciascuna risorsa.

    ![screenshot](images/craft-maxtiles.png)

## Sfida: Cambia le dimensioni del tuo mondo { .challenge}
Puoi cambiare i valori delle variabili "MAPWIDTH" e "MAPHEIGHT" per cambiare le dimensioni del mondo?

![screenshot](images/craft-mapsize.png)

## Salva il progetto {.save}

# Passo 3: Creazione di una nuova risorsa di legno { .activity}

Creiamo una nuova risorsa di legno. Per farlo, devi prima aggiungere delle variabili al tuo file"variables.py".

+ Per prima cosa devi dare un numero alla tua nuova risorsa. Potrai quindi usare la parola "WOOD" (che significa legno in inglese) nel codice, invece del numero 4.

    ![screenshot](images/craft-wood-const.png)

+ Devi aggiungere la tua nuova risorsa "WOOD" al tuo elenco di risorse in "resources".

    ![screenshot](images/craft-wood-resources.png)

+ Devi anche dare alla tua risorsa un nome che verrà visualizzato nell'inventario.

    ![screenshot](images/craft-wood-name.png)

    Nota che c'è una virgola alla fine della riga precedente.

+ La tua risorsa avrà anche bisogno di un'immagine. Il progetto contiene già un'immagine chiamata "wood.png" che dovresti aggiungere al tuo dizionario delle immagini ("textures").

    ![screenshot](images/craft-wood-texture.png)

+ Aggiungi il numero della tua risorsa che deve essere nell'inventario all'inizio.

    ![screenshot](images/craft-wood-inventory.png)

+ Per finire, aggiungi il tasto che bisogna premere per mettere il legno nel mondo. 

    ![screenshot](images/craft-wood-placekey.png)

+ Lancia il progetto per vedere se funziona. Vedrai che hai ora una nuova risorsa di legno ("wood") nell'inventario.

    ![screenshot](images/craft-wood-test.png)

+ Ma nel mondo di legno non ce n'è! Per correggere questo intoppo, fai clic sul file "main.py" e cerca la funzione denominata "generateRandomWorld()".

    ![screenshot](images/craft-wood-random1.png)    

    Questo codice genera un numero casuale compreso tra 0 e 10 e utilizza questo numero per decidere quali risorse inserire:

    + 1 o 2 = acqua
    + 3 o 4 = erba
    + tutti gli altri = terra

+ Aggiungi questo codice per aggiungere legno al mondo ogni volta che il numero casuale di "randomNumber" è 5.

    ![screenshot](images/craft-wood-random2.png)

+ Prova di nuovo il progetto. Questa volta dovresti vedere che del legno comincia ad apparire nel mondo.

    ![screenshot](images/craft-wood-test2.png)

## Sfida: Crea la sabbia { .challenge}
Puoi aggiungere una risorsa di sabbia ("SAND" in inglese) al gioco? Prova a usare guida la stessa procedura descritta qui sopra.

![screenshot](images/craft-sand.png)

Il progetto contiene già un'immagine di sabbia in "sand.png" ma puoi benissimo creare e caricare una tua immagine se lo preferisci.

![screenshot](images/craft-upload.png)

## Salva il progetto {.save}

# Passo 4: Fabbricare tavole di legno { .activity}

Creiamo adesso una nuova risorsa di tavole, che può essere fabbricata con il legno.

+ Per prima cosa, aggiungiamo la nuova variabile "PLANK" al gioco. Plank significa tavola in inglese.

    ![screenshot](images/craft-plank-const.png)

+ Aggiungi la nuova variabile "PLANK" al gioco. 

    ![screenshot](images/craft-plank-resources.png)

+ Chiama questa risorsa "plank" (tavola).

    ![screenshot](images/craft-plank-names.png)

+ Dai alla tua risorsa "PLANK" un'immagine. Il progetto contiene già un'immagine per la tavola in "plank.png" ma puoi benissimo creare una tua immagine se lo preferisci.

    ![screenshot](images/craft-plank-textures.png)

+ Aggiungi tavole all'inventario.

    ![screenshot](images/craft-plank-inventory.png)

+ Imposta un tasto per collocare tavole.

    ![screenshot](images/craft-plank-placekeys.png)

+ Dato che questa risorsa può essere fabbricata, devi creare una regola di fabbricazione, vale a dire, una tavola può essere fabbricata con 3 mattonelle di legno. Aggiungi questo codice al dizionario di fabbricazione "crafting". 

    ![screenshot](images/craft-plank-crafting.png)

+ Da ultimo, devi impostare un tasto per fabbricare nuove tavole.

    ![screenshot](images/craft-plank-craftkeys.png)

+ Per testare la tua nuova risorsa di tavole, raccogli qualche mattonella di legno e usale per fabbricare delle tavole. Colloca quindi le tue nuove tavole nel mondo.

    ![screenshot](images/craft-plank-test.png)

## Salva il progetto {.save}

## Sfida: Fabbricare il vetro con la sabbia { .challenge}
Prova a creare una nuova risorsa di vetro, che può essere fabbricata con la sabbia. Puoi farlo usando come guida la stessa procedura descritta qui sopra.

![screenshot](images/craft-glass.png)

Il progetto contiene già un'immagine per il vetro in "glass.png" ma puoi benissimo creare una tua immagine se lo preferisci.

## Salva il progetto {.save}

## Sfida: Crea altre risorse { .challenge}
Prova ad aggiungere al gioco altre risorse ed altre regole di fabbricazione.

## Salva il progetto {.save}