---
title: Secret Messages — Volunteer Notes
---

#Introduction:
In this project, children will learn how to make an encryption program, to send and receive secret messages with a friend. This project introduces iteration (looping) over a text string.

#Online Resources

__This project uses Python 3.__ We recommend using [trinket](https://trinket.io/) to write Python online. This project contains the following Trinkets:

+ [New (blank) Python Trinket -- jumpto.cc/python-new](http://jumpto.cc/python-new)

There is also a trinket containing the finished project:

+ [‘Secret Messages’ Finished -- trinket.io/python/402256078c](https://trinket.io/python/402256078c)

+ [‘Friendship Calculator’ Finished -- trinket.io/python/2e852cd687](https://trinket.io/python/2e852cd687)

#Offline Resources
This project can be [completed offline](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) if preferred.

You can find the completed project in the 'Volunteer Resources' section, which contains:

+ messages-finished/messages.py
+ messages-finished/friends.py

(All of the resources above are also downloadable as project and volunteer `.zip` files.)

#Learning Objectives
+ Iteration (looping) over a string variable;
+ The `find()` method;
+ The modulus operator (`%`).

This project covers elements from the following strands of the [Raspberry Pi Digital Making Curriculum](http://rpf.io/curriculum):

+ [Combine programming constructs to solve a problem.](https://www.raspberrypi.org/curriculum/programming/builder)

#Challenges
+ Use a Caesar cipher - encrypy and decrypt letters and words manually;
+ Variable keys - allowing the user to input a chosen key;
+ Encrypting and decrypting messages - encrypting and decrypting whole messages;
+ Friendship calculator - applying text iteration to a new problem.

#Frequently Asked Questions
+ When searching using `find()` or `if char in alphabet:`, note that searches are case-sensitive. Children can use:

	```python
	message = input("Please enter a message to encrypt: ").lower()
	```

	to make the input lower case before searching.