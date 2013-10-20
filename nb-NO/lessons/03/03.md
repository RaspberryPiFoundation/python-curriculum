#03—Hemmelige koder

Legg bort skilpaddene dine, i dag skal vi lære hvordan vi kan sende hemmelige beskjeder!

## Kodeklubb-koden

Et chiffer er et system for å gjøre om vanlig tekst til kode som ikke andre skal kunne lese. Vi skal her gjøre et av de eldste og mest berømte chifferene, Caesar-chifferet eller Caesars kode, etter Gaius Julius Caesar som sannsynligvis brukte dette for å sende hemmelige beskjeder. Det er neppe den beste metoden å sende beskjeder hvis du ikke vil at andre skal lese dem, men det kommer vi til. Det finnes ferdige moduler til Python du kan bruke hvis du vil lage noe som skal være vanskelig å knekke, men nå skal vi forsøke å lage Caesar-chifferet selv.


Start med å tegne alle bokstavene i en sirkel.

```
                          Å    A
                     Ø              B
                 Æ                      C
             Z                               D

         Y                                       E

      X                                             F

     W                                               G

     V                                               H

      U                                             I

         T                                       J

             S                               K
                R                        L
                    Q                M
                        P    O   N

```

For å lage en hemmelig bokstav fra en vanlig bokstav, trenger vi en hemmelig nøkkel. Jeg liker tallet 3, det er et magisk tall, så vi bruker det.

```
    A + 3 = D       T + 3 = W       Å + 3 = C
```

Vi begynner med A og teller fremover 3 bokstaver: B, C, D. Så bokstaven A blir til bokstaven D. For å dekode gjør vi det samme, men baklengs. Vi begynner med D og teller bakover for å få A.


## Oppgave 1: Alfabetet

Her kan du få trøbbel med norske bokstaver om du ikke har Python 3. Du ser det i IDLE, står det 2.6 eller 2.7 eller noe sånt har du Python 2. I så fall kan du enten installere 3 eller bare hoppe over norske bokstaver.

1. Først må vi lære python alfabetet. Åpne IDLE og lag en ny fil med koden
under:

    ```python
    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    print(len(alphabet))
    ```

2. Når du kjører dette programmet skal det skrive ut 29. Pass på at du har med alle bokstavene, ellers kommer ikke den hemmelige koden din til å virke.

    Hvis du er fornøyd med alfabetet ditt kan vi begynne å kode en bokstav.

## Oppgave 2: Kode en bokstav

1. Akkurat som vi gjorde med hjulet ovenfor kan vi finne posisjonen til en bokstav ved å telle forover, og så bruke bokstaven vi ender opp med.

    Skriv inn koden under og kjør den:

    ```python
    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    letter = "a"
    secret = 3

    pos = alphabet.find(letter)

    newpos = (pos + secret)

    if newpos >= 29:
        newpos = newpos - 29

    secretletter = alphabet[newpos]

    print(secretletter)
    ```

    Vi slår opp hvor "a" er i alfabetet og legger til det hemmelige tallet vårt for å telle fremover. Vi sjekker om vi har gått rundt, hvis vi har det må vi gå en hel runde tilbake igjen ved å trekke fra 29 (dette er litt som med gradene, å trekke fra 360 gjør at vi er akkurat der vi var). Så slår vi opp i alfabetet igjen for å se hvilken hemmelige bokstav vi fikk.

2. Kjør koden og se hva som skjer.

3. La oss ta en titt på koden igjen, men vi tar det sakte.

    Du trenger ikke å skrive dette! Alt som står bak firkanten bryr python seg vanligvis ikke om, det er bare kommentarer til mennesker som skal lese koden.

    ```python

    # alphabet er navnet på teksten fra a til å
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Den hemmelige bokstaven (letter) og det hemmelige tallet (secret) vi
    # bruker for å kode det
    letter = "a"
    secret = 3

    # Finn posisjonen til bokstaven
    # og python vil gi oss et tall fra 0 til 28 (python teller fra 0)
    pos = alphabet.find(letter)

    # gå like langt fremover som det hemmelige tallet sier vi skal
    newpos = (pos + secret)

    # Hvis vi har telt for langt, må vi gå en runde tilbake for å få et tall
    # mellom 0 og 28
    if newpos >= 29:
        newpos = newpos - 29

    # Slå opp denne posisjonen for å se hvilken bokstav i alfabetet som står
    # der
    secretletter = alphabet[newpos]

    # og skriv dette ut på skjermen
    print(secretletter)
    ```

    Det er mye python-ting som skjer her, men ikke bli skremt om du ikke forstår alt til å begynne med. Mye av dette er akkurat som i scratch. `if newpos >= 29` er bare en `if` setning, en ting som bare kjører koden under hvis det som står etter if er sant. If bruker en innrykksblokk, akkurat som `for` og `def` som vi har sett tidligere.


Nå som vi kan kode en bokstav, hva med å dekode en?

## Oppgave 3: Finne tilbake bokstavene

Akkurat som i koden fra den forrige oppgaven skal vi finne posisjonen til bokstaven, men denne gangen skal vi gå bakover i alfabetet for å dekode.

1. Forsøk å skriv inn denne koden og kjør den:

    ```python
    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    secret =17
    secretletter = "r"

    pos = alphabet.find(secretletter)

    newpos = pos - secret

    if newpos < 0:
        newpos = newpos + 29

    letter = alphabet[newpos]

    print(letter)
    ```

## Oppgave 4: Bygge funksjoner

Oppgave: Ser du hvorfor dette er en funksjon og ikke en prosedyre? De ser helt like ut, men de har noen forskjellige egenskaper likevel. Dette spiller ikke så stor rolle nå, men det er like greit å lære seg forskjellen nå.

La oss ta den første koden (som laget kode av bokstaver) å lage det til en
funksjon 'encode' og den andre koden til en funksjon `decode`. Vi laget
hvordan vi definerte prosedyrer i modul to. For å få den til å returnere en
verdi som vi kan bruke senere, bruker vi kommandoen `return`.

Prosedyrer bare gjør ting, og funksjoner beregner ting. Noen ganger blander man det også sammen og lager prosedyrer som både beregner og gjør ting, men jo mer du kan skille disse fra hverandre jo enklere blir programmet ditt både for deg å andre. Det vi lager nå er funksjoner, fordi de ikke bare beregner en verdi, de skriver ingenting ut, de tegner ingenting på skjermen og resultatet blir likt hver eneste gang hvis man gir inn samme bokstav og hemmelige tall.

1. Lag en fil som ser slik ut:

    ```python
    alphabet = "abcdefghijklmnopqrstuvwxyzæøå"

    def encode(letter, secret):
        pos = alphabet.find(letter)

        newpos = (pos + secret)

        if newpos >= 29:
            newpos = newpos - 29

        return alphabet[newpos]



    def decode(letter, secret):
        pos = alphabet.find(letter)

        newpos = (pos - secret)

        if newpos < 0:
            newpos = newpos + 29

        return alphabet[newpos]

    print(encode("a", 17))
    print(decode("r", 17))
    ```

    Husk at du kan bruke Tab i Idle for å få innrykk. Du kan også merke deler av koden og rykke alt inn på en gang.

2. Prøv å kode og dekode noen bokstaver!


## Oppgave 5: Send ett hemmelig ord eller to, og finn dem tilbake igjen

Nå har vi noen funksjoner, la oss bruke dem til å kode ord. Vi kommer til å gå igjennom hver bokstav i ordet og kode det hvis det finnes i alfabetet (vi hopper over tegn som punktum og mellomrom).

1. Under de nye funksjonene fra forrige oppgave kan du skrive inn koden under (altså behold det du gjorde i oppgave 4).

    ```python

    secret = 17
    message = "hello world"

    output = ""

    for character in message:
        if character in alphabet:
            output = output +  encode(character, secret)
        else:
            output = output + character


    print(output)

    secret = 17
    message = "yvååc kcfåu"
    output = ""

    for character in message:
        if character in alphabet:
            output = output + decode(character, secret)
        else:
            output = output + character

    print(output)
    ```

2. Kjør programmet og se hva som skjer

    Den første delen av koden burde skrive ut "yvååc kcfåu", som er den hemmelige versjonen av "hello world". Den andre delen dekoder det igjen og skriver ut "hello world"

## Oppgave 6: Dekoding av noen hemmelige beskjeder

Her er noen hemmelige beskjeder, forsøk å dekode dem!

1. `daczj ym cgyzcdmwwzf?`, hemmeligheten er 21.

2. `æxkxånwn næ bnwwnwn mrwn`, hemmeligheten er 9.

Prøv og send noen beskjeder til vennene dine! Hva med å lage et Python program som forsøker seg på alle mulige hemmelige tall og forsøker å knekke koder selv om du ikke kan det hemmelige tallet?
