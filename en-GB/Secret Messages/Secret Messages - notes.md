---
title: Secret Messages — Notes for Club Leaders
language: en
embeds: "*.png"
...

#Introduction:
This project teaches iteration over a text string, and now it can be used to create a Caesar cipher.

#Resources
For this project, Python will need to be installed. It is recommended that version 3.2 of Python is installed.

Children can also make use of the materials which accompany these challenges. Files included in the 'Project Resources' folder (found under the 'Download Project Materials' link):

+ Encryption.py

Make sure that each child has read and write access to their own copy of these resources.

You can find a completed version of this project's challenges by clicking the 'Download Project Materials' link for this project, which contains:

+ LoveCalculator.py

#Learning Objectives
+ Iteration over a string variable;
+ The `find()` method;
+ The modulus operator (`%`).

#Challenges
+ Variable keys - allowing the user to input a chosen key;
+ Encrypting and decrypting characters - single character encrypting and decrypting;
+ Encrypting and decrypting messages - encrypting and decrypting whole messages;
+ Improving your cipher - modifying the program to make cracking the cipher more difficult;
+ Love calculator - applying text iteration to a new problem.

#Frequently Asked Questions
+ When searching using `find()` or `if char in alphabet:`, note that searches are case-sensitive. Children should use:

```python
message = input("Please enter a message to encrypt: ").lower()
```

to make the input lower case before searching.