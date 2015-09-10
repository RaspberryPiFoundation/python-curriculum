print(" Love Calculator ")
print("<3 <3 <3 <3 <3 <3")

names = input("\nEnter the names of 2 people: ")
score = 0

for char in names:

    if char in "loves":
        score += 10

    if char in "fhvwy":
        score += 5

    if char in "aeiou":
        score += 3
        
    if char in "z":
        score += 10    

print("Your compatibility score is" , score)
