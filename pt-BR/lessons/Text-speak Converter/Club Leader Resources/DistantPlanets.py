distances = {
    "mercúrio"   : 91700000,
    "marte"      : 54600000
}

planet = input("Digite um planeta: ").lower()
distance = distances[planet]

print(planet , "está a" , distance , "km da Terra")
