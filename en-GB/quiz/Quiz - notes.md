---
title: Quiz — Notes for Club Leaders
language: en
embeds: "*.png"
...

#Introduction:
This project teaches children how to use selection (`if`, `else` and `elif` statements) in their programs, to alter program flow in response to data. This is achieved through writing and testing a simple quiz program, which includes written text and multiple choice responses.

#Resources
For this project, Python will need to be installed. It is recommended that version 3.2 of Python is installed.

Children can also make use of the materials which accompany this project. Files included in the 'Project Resources' folder (found under the 'Download Project Materials' link):

+ Quiz.py

Make sure that each child has read and write access to their own copy of these resources.

#Learning Objectives
+ Selection, using:
	+ `if`;
	+ `else`;
	+ `elif`.
+ Program testing and problem solving.

#Challenges
+ Question time - using `if` and `else` to give quiz answer feedback;
+ Fixing your quiz - use of the `.lower()` method to reduce errors in answer feedback;
+ Multiple choice quiz - using `elif` to add multiple choice quiz questions;
+ Keeping score - addition of a `score` variable to track progress;
+ How did I do? - further use of `if` and `else` statements to provide an end of quiz message, based on their score.

#Frequently Asked Questions
+ As the player's input is stored as text, any questions with a numerical answer should also be represented as text. For example:

```python
if answer == "4":
	...
```

and *not*:

```python
if answer == 4:
	...
```

As an alternative, it is also possible to cast the player's answer to a number, and then compare the two numbers:

```python
answer = int(answer)
if answer == 4:
	...
```

+ Each `if`/`else`/`elif` statement should end with a colon.

+ The body of each `if`/`else`/`elif` statement should be uniformly indented. It is recommended that the Tab key is used for this, as it makes indentation mistakes easier to spot. For example, the following program will not run:

```python
if answer == "variable":
   print("Well done")
  print("---------")
    print(" :) ")
 )
```

+ Children should remember the difference between `=` (used for variable assignment) and `==` (used for checking equality).