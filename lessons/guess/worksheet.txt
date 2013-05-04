Intro
-----
Now for something completely different! We are going to use a programming language called 'Python' to write a game where you can play against the computer in a number guessing game.  The computer will always be able to guess your number in 7 goes - can you do the same?

Firstly, there are a few things you need to know about Python before you start.

Python basics
-------------
Unlike Scratch, you don't need to load a Python program to start writing code. Your code can be written in any "text editor" program, such as 'notepad'. When you have written your code, you can run it in a number of ways - if you are using Windows you could open a command window and type:

python myprogram.py

Your program will be a list of instructions (or statements) for the computer to follow. We will learn lots of different statements, but before we start:

Every program will start with a line similar to:

#!/usr/bin/env python

This line is used by some computers to know how to run Python programs

Any line that starts with a '#' are ignored by Python. You can use this to put comments about how the code works. You should do this a lot, so that other people (and you!) can understand how your code is supposed to work!

Identation is important!  You will see that lots of lines of Python code start with some spaces. This is used to know which code belongs together. For example:
 
    if score > highscore:
        highscore = score
    score = 0
        
The second line 'belongs' to the 'if' statement - it will only be executed when score is greater than highscore. However, because the last line is not indented as much, it does not belong to the 'if' statement.

Step 1 - Get Python to say something
-------------------------------------
A useful Python statement is 'print'.  This tells Python to write something on the screen, and can be used to tell us what is happening. Create a text file called YouGuess.py, and type the following code into it:

#!/usr/bin/env python

    #First print out a message to say hello
print 'Hello.  I hope you are well today.'
print 'I am thinking of a whole number, between 1 and 100 inclusive'
print 'I will give you 8 goes at guessing it, and tell you whether it is higher or lower than your guess'
print '(I am feeling generous, you should only need 7 goes)'

You can change the words that are printed out to whatever you want.

Be careful!  The words to be printed out start and end with '  If you use this character in the words as an apostophy, Python will think that is the end of the words, and get confused! So if you want to write "I'm", so need to put a "\" before the apostophy:

print 'I'm a happy bunny.'     #This Won't work
print 'I\'m a happy bunny.'    #This will work, and won't print the \

Also, you can put \n in the words to start a new line:

print 'First line \nsecond line'

Test your code! how to do this will depend on your computer, but it may be typing "python youguess.py" in a command window.

If you see the words being printed out, CONGRATULATIONS - you have written a working Python program!  Try changing the words, and put some new lines in to make the output look nicer.

Step 2 - Variables
------------------

Just like in Scratch, Python programs use variables to keep track of numbers. We can make a variable just by giving a name a number with the equals sign:

    score = 1000
    
For this game, we need to choose the number the user must guess. Let's say:

    correct = 42
    
To check this has worked, we can print the variable out:

    Print 'Don\'t tell anybody, but I\'m thinking of the number ', correct

Put these statements into your code and run it.  Does it work?

The game won't be very good if the computer always thinks of the number 42 though! We need to make it think of a different number each time, which we can do by creating a "random" number. The function we need to do this is automatically available in Python - we have to say we want to use the "random" module.  We do this by putting an "import" statement before our print statements:

#Import Modules
import random

Now we can use a function in the random module to choose our number. Change the line creating the "correct" variable to:

    correct = random.randint(1,100)     #Choose a random number between 1 and 1000
    
Test you code!  Do you get a different number every time?

Step 3 - you get 8 chances
--------------------------
Now we need to let the user type in their guesses, and tell them whether the correct answer is bigger or smaller. We want to give them 8 chances, so we want a loop that runs 8 times. This can be done with a 'for' loop:

for go in range (1, 9):

In this statement, "go" is a variable name - we can call this anything we like. All of the code after this statement that is idented more than it, will be run 8 times. Each time through "go" will a differnt value from 1 to 8 (the 9 in the code is NOT a mistake - the last number is not included).

Each time we run the loop, we want to tell the user which go they are on (from the variable go), and ask for their guess. We can do that with the statement:

    guess = input('Guess number '+str(go)+':')
    
This will print out "Guess number 1: ", then wait for a number to be typed in. The number entered will be put in the variable "guess".

Test your code! Does it ask for the right number of guesses?  Try changing what is printed out to ask for the guess.

Now we need the computer to tell us whether the correct answer is bigger or smaller than our guess. We can use an "if" statement to work this out.  Add this code to your "for" loop (be careful with indentation!

for go in range (1, 9):
    guess = input('Guess number '+str(go)+':')
    if guess < correct:
	print 'It\'s bigger than', guess
    if guess > correct:
	print 'It\'s smaller than', guess
    if guess == correct:
	print 'Correct!  Brilliant, you are so clever!'
	
Test your code! Does it correctly tell you whether you need a bigger or smaller number? What happens when you get the answer right?

Of course, once we've guessed the right answer, the computer should stop asking. We can do this by adding a "break" statement after the print to say we are right. This means stop running the loop straight away, even if we haven't got to the last number.

Finally, if you don't guess the number in 8 goes, the computer wins and should tell us so. We can do this with an "else" statement after the for loop. This code will only run if we get to the end of the for loop without doing a "break".

for go in range (1, 9):
    guess = input('Guess number '+str(go)+':')
    if guess < correct:
	print 'It\'s bigger than', guess
    if guess > correct:
	print 'It\'s smaller than', guess
    if guess == correct:
	print 'Correct!  Brilliant, you are so clever!'
	break
else:
    print 'That\'s all your goes, and you didn\'t guess it - I win!'
    
Test your code! Does it tell you correctly whether you win or lose?  Try taking out the print to tell you what the number is - can you beat the computer?

Step 4 - the comupter's turn to guess
-------------------------------------

Now let's write the game the other way round! Create a new program called "Iguess.py". It may be easiest to copy "youguess.py", and delete the code you don't want.

We still want the print statements to say hello, but they need to describe the game the other way round (the computer guesses). We also still want a for loop for 8 goes, but what is in the for loop will change. You code should look something like:

#!/usr/bin/env python

print '\n\nHello.  I hope you are well today.\nLet\'s play a game of "guess my number"\n\n'
print 'You think of a whole number, between 1 and 100 inclusive'
print 'I\'ll guess at your number, and you tell yme whether it\'s higher or lower than my guess'
print 'Type h if your your number is higher then my guess,\nType l if it\'s lower and\nType c if I guess it correctly.'
print '\n\nDon\'t cheat!!!\n\n'

for go in range (1, 9):


How is the computer going to make it's guess?  First, we need two variables to store the numbers we know the answer is greater than and less than. To start with, we only know the answer is greater than 0, and less than 101. Create two variables before the "for" loop:

greaterthan = 0
lessthan = 101

A sensible guess to make is half way between these two numbers. We can do this by adding the two numbers together, and dividing the answer by 2. Create a variable in the for loop calculates a guess this way:

for go in range (1, 9):
    guess = (greaterthan + lessthan)/2
    
Now we need to tell the user this number, and ask whether the answer is lower or higher. This time we need to use "raw_input", because the "input" function we used before only lets us enter numbers:

    response = raw_input('Guess number '+str(go)+' is '+str(guess)+': ')
    
If the user says the answer is higher, we can change the "greaterthan" variable to the number we guessed. If the user says lower, we can change the "lessthan" variable. This will let us make a better guess next time.

If the user says we are correct, we can print out a happy message. As before, we then want to "break" so stop guessing. This can all be done with 3 if statements in our loop:

    if response == 'h':
	greaterthan = guess
    if response == 'l':
	lessthan = guess
    if response == 'c':
	print 'Yeah - I love it when I\'m right!'
	break
	
If our code works correctly, it should always get the right answer in less than 8 goes. However, in case something goes wrong we can add an "else" statement to tell us:

else:
    print 'It\'s not fair!'         # Should never get here
    
Test your code! Does the computer guess your number every time?

Step 5 - Any cheating going on?
-------------------------------
What happens if you don't answer the computer correctly. Try saying your number is less than the first guess (50), but then always say higher, even when it guesses 49?

The program things the number has to be more than 49, and that it has to be less than 50! It has to pick a number, and it chooses 49. We can use this to detect if the users answers don't make sense. If the guess is the same as "lessthan" or "greaterthan", the user must have got the answers wrong. Add this code after you calculate the guess:

Test your code! Now if you get the answers wrong, does the program let you know?

Step 6 - Take it in turns
-------------------------
It would be nice to take it turns to guess, and let the computer guess. That way we can see who's best!  We could do that by putting both programs in the same file after each other, then putting a loop around them. However, this would be very difficult code to read!

We can do better by making each of our programs into a function. A function gives a name to a section of code, then we can run that code somewhere else by using it's name.  To make the code into a function, we need to put a "def" statement before it:

def iguess():

All of the code in the function then needs to be idented so we know it is part of this function. In this example the name of the function is iguess.  Later we will see why you need to have the brackets.

Create a new file called weguess.py. Paste the code from both youguess.py and iguess.py into this file (but we only need one copy of the  "#!/usr/bin/env python" line and the import line.

Now make each part a function by add def statements to make functions called youguess and iguess. You will need to indent all of the code - in most editors you can do this by selecting the code and pressing the "tab" button.

Try running the code. It should not do anything at all!  This is because "def" tells Python to create this function, but it doesn't say to run it!  We can add some code beneath the function definitions to print out a wekcome, then call each of the functions in turn.

print '\n\nHello.  I hope you are well today.\nLet\'s play a game of "guess my number"\n\n'
while True:
    iguess()
    youguess()

The "while True:" creates a loop that will carry on forever! Make sure this line is not idented, so that it is not part of the function before it.

Test your code!  Does it play each version of the game in turn?  Does it ever end? Do might the messages print out still make sense? You might need to remove a print statement from each function so that it doesn't keep saying hello!

To end the program, you can press the ctrl key and 'c'.

Further ideas:

1) Add a score to keep track of whether you are better than the computer
2) Maybe the computer is too good at guessing your number! Can you use the random number function to make it not quite so good?







