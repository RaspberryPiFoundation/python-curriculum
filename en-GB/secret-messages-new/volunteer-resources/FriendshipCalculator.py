print(" Friendship Calculator ")
print(" ===================== ")

names = input("\nEnter the names of 2 people: ")
score = 0

for char in names:

    if char in "friend":
        score += 10

    if char in "aeiou":
        score += 3
        
    if char in "z":
        score += 10    

print("Your friendship score is" , score)

if score > 100:
	print "Best friends!"
