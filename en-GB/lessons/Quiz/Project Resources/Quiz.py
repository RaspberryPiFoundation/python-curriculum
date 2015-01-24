print("In Python, what do you call a 'box' used to store data?")
answer = input()

if answer == "variable":
	print(" :) ")
else:
	print(" :( ")

print("Thank you for playing!")


print('''
Q1 - In Python, what do you call a 'box' used to store data?
a - text
b - variable
c - a shoe box
''')
answer = input().lower()

if answer == "a":
	print(" Nope - text is a type of data :( ")
elif answer == "b":
	print(" Correct!! :) ")
elif answer == "c":
	print(" Don't be silly! :( ")
else:
	print(" You didn't choose a, b or c :( ")
