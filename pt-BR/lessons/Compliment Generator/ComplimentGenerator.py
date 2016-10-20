import random

print("Gerador de Cumprimentos")
print("--------------------")

cumprimentos = [ "Excelente trabalho. Realmente muito bem feito." ,
                "Suas habilidades de programação são muito, muito boas." ,
                "Você é um humano excelente."
              ]

#imprime um item aleatório da lista 'cumprimentos'
print(random.choice(cumprimentos))
print("De nada!")
