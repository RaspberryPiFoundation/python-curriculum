print(" Kalkulator Milosci ")
print("<3 <3 <3 <3 <3 <3 <3")

imiona = input("\nWprowadz imiona dwojga ludzi: ")
punkty = 0

for litera in imiona:

    if litera in "kocha":
        punkty += 10

    if litera in "fhvwy":
        punkty += 5

    if litera in "aeiou":
        punkty += 3
        
    if litera in "z":
        punkty += 10    

print("Wasze punkty zgodnosci wynosza " , punkty)
