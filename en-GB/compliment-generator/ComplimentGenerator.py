import random

print("Compliment Generator")
print("--------------------")

compliments = [ "Great job on that thing you did. Really super." ,
                "You have really really nice programming skills." ,
                "You make an excellent human."
              ]

#print a random item in the 'compliments' list
print(random.choice(compliments))
print("You're welcome!")
