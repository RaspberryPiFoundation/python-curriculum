# 05 — Hangman

La oss lage et spill: Hangman! Datamaskinen vil velge et ord, og du kan gjette det bokstav for bokstav. Men dersom du gjetter feil for mange ganger taper du.

## Steg 1: Velg et ord

Først må vi få datamaskinen til å velge et tilfeldig ord, så la oss begynne.

1. Åpne IDLE, og åpne et nytt vindu

2. Skriv inn følgende kode:

    ```python
    from random import choice

    word = choice(["code", "club"])

    print(word)
    ```

3. Lagre programmet ditt, og kjør det. Hvilket ord skrives ut?

4. Kjør programmet en gang til. Skriver det ut et annet ord?

Hver gang du kjører dette programmet vil det velge et tilfeldig ord fra listen `["code", "club"]`, ved hjelp av `choice`-funksjonen.

## Steg 2: Gjett en bokstav

Nå har vi valgt et ord, la oss finne ut hvordan vi gjetter en bokstav.

1. I den samme filen, endre koden så den ser ut som følger

    ```python
    from random import choice

    word = choice(["code", "club"])

    out = ""

    for letter in word:
        out = out + "_"

    print("Guess a letter in the word:", out)
    ```

2. Lagre og kjør programmet.

3. You should see "Guess a letter in the word: ____", in the output window (the other window, not the one you've written your program in.)

    We use a for loop to build up some text with an underscore `_` for each letter in the word. The word "code" put in, will write out `____` to the screen.


4. Let's guess a letter! Change the code to look like this

    ```python
    from random import choice

    word = choice(["code", "club"])

    out = ""

    for letter in word:
        out = out + "_"

    print("Guess a letter in the word, then press enter:", out)

    guess = input()

    if guess in word:
        print("Yay")
    else:
        print("Nope")
    ``` 

    We use a new function `input()` to find out what the player typed. We use `if` to find out if the letter was in the word.

We've got the essentials down, so let's continue onward. 

(Python 2 Note: Use `raw_input` if you're on an old version of python)

## Step 3: Track the guesses

Now we're going to use two features of python, lists and the `while` loop. 

1. In the same file, edit the code to look like this:

    ```python
    from random import choice

    word = choice(["code", "club"])

    guessed = []

    while True:

        out = ""
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == word:
            print("You guessed", word)
            break
            

        print("Guess the word:", out)
        guess = input()

        if guess in guessed:
            print("Already guessed", guess)
        elif guess in word:
            print("Yay")
            guessed.append(guess)
        else:
            print("Nope")

        print()
    ```

2. Run the code, try guessing the letters. 

    What we've done is put a loop, like `forever` in scratch, that will keep asking for letters from the player, until they guess the word.

    We also use a list, `guessed`, which we add the letters to when they're right. This program will loop forever until all the letters are guessed.


## Step 4: Track the mistakes

Hangman should only give you a few chances to guess, rather than trying every letter in turn

1. Edit the existing file, and change it to look like the following:

    ```python
    from random import choice

    word = choice(["code", "club"])

    guessed = []
    wrong = []

    while True:

        out = ""
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == word:
            print("You guessed", word)
            break

        print("Guess the word:", out)

        guess = input()

        if guess in guessed or guess in wrong:
            print("Already guessed", guess)
        elif guess in word:
            print("Yay")
            guessed.append(guess)
        else:
            print("Nope")
            wrong.append(guess)

        print()

    ```
    We're using a new list, `wrong`, to store all the guesses that weren't right

Only one last thing before the game is complete, which is to only have a few chances to guess.

## Step 5: Only a few chances

1. Edit the file, to introduce a new variable, `tries`:

    ```python
    from random import choice

    word = choice(["code", "club"])

    guessed = []
    wrong = []

    tries = 7

    while tries > 0:

        out = ""
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == word:
            break

        print("Guess the word:", out)
        print(tries, "chances left")

        guess = input()

        if guess in guessed or guess in wrong:
            print("Already guessed", guess)
        elif guess in word:
            print("Yay")
            guessed.append(guess)
        else:
            print("Nope")
            tries = tries - 1 
            wrong.append(guess)

        print()

    if tries:
        print("You guessed", word)
    else:
        print("You didn't get", word)
    ```

2. Run the file, and see what happens when you guess wrong letters

## Step 6: Add some new words in

1. Find the line in the source code:

    ```python
    word = choice(["code", "club"])
    ```

2. Edit it to add more words, why not try

    ```python
    word = choice(["code", "club", "robot", "party"])
    ```
    
    Remember to put the words in quotes, and put a comma between them to make a list of words.



