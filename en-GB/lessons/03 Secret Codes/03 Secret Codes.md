---
title: Secret Codes
level: Level 2
language: en
stylesheet: python
...

# Introduction { .intro}
Put your turtles away, today we're going to learn how to send secret messages!

# The Code Club Cipher { .activity}

A cipher is a type of secret code, where you swap the letters around so no-one can read your message. We'll be doing one of the oldest and most famous ciphers, the Caesar Code. Named after a famous person, not Dog food.

We start by drawing the letters in a circle.

```
                        Z    A    B
                  Y                     C
             X                               D

         W                                       E

      V                                             F

     U                                               G

     T                                               H

      S                                             I

         R                                       J

             Q                               K
                  P                     L
                        O    N    M
```

To make a secret letter from a normal one, we need to have a secret key. For our example let's use the number 3.

```
    A + 3 = D       T + 3 = W       Z + 3 = C
```

We start at A, and count forward 3 letters: B, C, D. So the letter A turns into the letter D.  To decode, we do the same thing, but in reverse. We start at D and count backwards to get A.

# Task 1: The Alphabet { .activity}

## Activity Checklist { .check}

+ First we'll have to tell python the alphabet. Open up IDLE, create and save a new file with the following code.
```{.language-python}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    print(len(alphabet))
```
+ When you run it (from the menu), it should print 2+ Make sure you've got all the letters in, or your secret code won't work. If you're happy with your alphabet, we can start to encode a letter.

# Task 2: Encoding a letter { .activity}

## Activity Checklist { .check}

+ Like on the wheel above, we find the position of the letter, we count forwards, and then use the letter we end up at. Write in the code below and run it:
```{.language-python}
alphabet = "abcdefghijklmnopqrstuvwxyz"

    letter = "a"
    secret = 3

    pos = alphabet.find(letter)

    newpos = (pos + secret)

    if newpos >= 26:
        newpos = newpos - 26

    secretletter = alphabet[newpos]

    print(secretletter)
```

We look up where "a" occurs in the alphabet, add the secret number to count forwards, check to see if we've gone too far, and then look up the letter again.

+ Run the code, and see what happens.
+ Let's look at the code again, but take it slowly.

You don't have to type this in!

```{.language-python}
# alphabet is the name for the text of a to z
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # the letter and secret we'll use to encode it
    letter = "a"
    secret = 3

    # find the position of the letter, and
    # python will tell us a number from 0 to 25
    pos = alphabet.find(letter)

    # we count forward a few letters
    newpos = (pos + secret)

    # if we count too far, we'll have to start
    # from the beginning
    if newpos >= 26:
        newpos = newpos - 26

    # now we look up the letter at this new pos
    secretletter = alphabet[newpos]

    # and output it to the screen
    print(secretletter)
```

There is a lot of python going on here, so don't worry if it seems a bit too much to understand at first. Much of is quite like scratch. `if newpos >= 26` is just an `if` statement, a thing that only runs the code underneath if the condition is correct. It uses an indented block, just like `for` and `def` that we've seen earlier.

Now we can encode a letter, how about decoding one?

# Task 3: Uncovering the letters { .activity}

Like the code from the earlier task, we find the position of the letter, but we go backwards through the alphabet to decode.

## Activity Checklist { .check}

+ Try copying the following code in and running it!
```{.language-python}
alphabet = "abcdefghijklmnopqrstuvwxyz"

    secret =17
    secretletter = "r"

    pos = alphabet.find(secretletter)

    newpos = pos - secret

    if newpos < 0:
        newpos = newpos + 26

    letter = alphabet[newpos]

    print(letter)
```

# Task 4: Building functions { .activity}

Now we can wrap these bits of codes in functions. Take the first code and make it a function `encode`, and the second one in `decode`. We learned how to define new functions in lesson two, but we're going to use a special command in python, `return`.

Some functions just do things, other functions can calculate things. Although we've looked at passing in values to a function, we haven't looked at handing back a result. Using `return` we can say that the function is complete and what the result is. It is called `return` because we are returning a value.

## Activity Checklist { .check}

+ Copy and paste the earlier code into a new file, and edit it to look like this:
```{.language-python}
alphabet = "abcdefghijklmnopqrstuvwxyz"

    def encode(letter, secret):
        pos = alphabet.find(letter)

        newpos = (pos + secret)

        if newpos >= 26:
            newpos = newpos - 26

        return alphabet[newpos]



    def decode(letter, secret):
        pos = alphabet.find(letter)

        newpos = (pos - secret)

        if newpos < 0:
            newpos = newpos + 26

        return alphabet[newpos]

    print(encode("a", 17))
    print(decode("r", 17))
```

Remember you can use the Tab key in Idle to indent code (and selections too)

+ Try encoding and decoding some letters!

# Task 5: Sending a Secret Word or two, and back again { .activity}

Now we have some functions, let's use them to encode words. What we're going to do is go through each letter in the word, and encode it if it's in the alphabet (so we skip spaces and punctuation)

## Activity Checklist { .check}

+ Underneath the new functions in the last Task, write the following code in the same file:
```{.language-python}
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
    message = "yvccf nficu"
    output = ""

    for character in message:
        if character in alphabet:
            output = output + decode(character, secret)
        else:
            output = output + character

    print(output)
```

+ Run it and see what happens.

The first bit of code should print "yvccf nficu", which is the secret version of "hello world". The second bit decodes it back, and should print "hello world"

# Task 6: Decode some secret messages { .activity}

## Here are some secret messages to try and decode! { .challenge}

+ `n frperg clguba`, the secret is 13.
+ `yj tjp gdfz xjyz xgpw?`, the secret is 21.
+ `axkxcb jan hxda oarnwmb`, the secret is 9.

## Try { .try}

Why not try and send your own secret messages?
