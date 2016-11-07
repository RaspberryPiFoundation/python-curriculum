def mostrarInstrucoes():
    #imprime um menu principal e os comandos
    print("Jogo de RPG")
    print("========")
    print("Comandos:")
    print("   ir [direção]")
    print("   pegar [item]")

def mostrarStatus():
    #imprime o status atual do jogador
    print("---------------------------")
    print("Você está na " + locais[localAtual]["nome"])
    #imprime o inventário atual
    print("Inventário : " + str(inventario))
    #imprime um item, caso haja algum
    if "item" in locais[localAtual]:
        print("Você está vendo um(a) " + locais[localAtual]["item"])
    print("---------------------------")

#um inventário, que está inicialmente vazio
inventario = []

#um dicionário que liga um cômodo a outro
locais = {

            1 : {  "nome"  : "Sala" ,
                   "sul" : 2 ,
                   "leste"  : 4 ,
                   "item"  : "chave"
                } ,        

            2 : {  "nome"  : "Cozinha" ,
                   "norte" : 1 ,
                   "leste"  : 3
                } ,

            3 : {  "nome" : "Sala de jantar" ,
                   "oeste" : 2 ,
                   "leste" : 5 ,
                   "sul" : 6 ,
                   "item" : "escudo"
                } ,

            4 : {  "nome"  : "Sala de estar" ,
                   "oeste"  : 1
                } ,

            5 : {  "nome"  : "Biblioteca" ,
                   "oeste"  : 3
                } ,

            6 : {  "nome"  : "Jardim" ,
                   "norte"  : 3
                }
         }

#inicia o jogador no cômodo 1
localAtual = 1

mostrarInstrucoes()

#laço infinito
while True:

    mostrarStatus()

    #obtem o próximo 'movimento' do jogador
    #.split() faz a quebra em uma lista
    #por exemplo: 'ir para o leste' retornaria a lista:
    #['ir','leste']
    move = input(">").lower().split()

    #Se digitarem 'ir' primeiro
    if move[0] == "ir":
        #verifica se é permitido ir para o local desejado
        if move[1] in locais[localAtual]:
            #define o local atual com o novo cômodo
            localAtual = locais[localAtual][move[1]]
        #não há nenhuma porta (link) para o novo cômodo
        else:
            print("Você não pode ir por esse caminho!")

    #se digitarem 'pegar' primeiro
    if move[0] == "pegar" :
        #se o cômodo contém um item, e este item é o mesmo que o jogador quer pegar
        if "item" in locais[localAtual] and move[1] in locais[localAtual]["item"]:
            #adiciona o item ao inventário
            inventario += [move[1]]
            #exibe uma mensagem de ajuda
            print(move[1] + " obtido(a)!")
            #remove o item do cômodo
            del locais[localAtual]["item"]
        #caso contrário, se não houver item para pegar
        else:
            #diga que o item não pode ser obtido
            print("Não foi possível pegar " + move[1] + "!")
