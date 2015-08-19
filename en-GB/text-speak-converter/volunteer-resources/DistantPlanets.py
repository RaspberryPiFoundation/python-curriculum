distances = {
    "mercury"   : 91700000,
    "mars"      : 54600000
}

planet = input("Enter a planet: ").lower()
distance = distances[planet]

print(planet , "is" , distance , "km from the Earth")
