from random import *

#essa variável deve ser alterada pelo usuário para terminar o jogo
playing = True

score = 0

#imprime as instruções do jogo
print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

#repete enquanto a variável 'playing' for 'True'
while playing == True:

    #escolhe um numero aleatoriamente entre 1 e 10
    newNumber = randint(1,10)

    #soma o novo número à pontuação
    score = score + newNumber

    #mostra os dados para o jogador
    print("\nSeu próximo número é", newNumber)
    print("Sua pontuação agora é", score)

    #termina se o usuário digitar 'n'
    #ou se a pontuação for maior que 21
    print("\nGostaria de somar mais um número? (s/n)")
    answer = input()
    if answer.lower() == 'n' or score > 21:
        playing = False
    
print("\nSua pontuação final é", score)

#se o jogador marcar 21
if score == 21:
    print("VOCÊ VENCEU!!")
else:
    print("Que pena!")
