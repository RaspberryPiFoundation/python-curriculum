print(" Calculadora do Amor ")
print("<3 <3 <3 <3 <3 <3")

nomes = input("\nDigite o nome de 2 pessoas: ")
grauDeCompatibilidade = 0

for char in nomes:

    if char in "amor":
        grauDeCompatibilidade += 10

    if char in "fhvwy":
        grauDeCompatibilidade += 5

    if char in "aeiou":
        grauDeCompatibilidade += 3
        
    if char in "z":
        grauDeCompatibilidade += 10    

print("Seu grau de compatibilidade é" , grauDeCompatibilidade)
