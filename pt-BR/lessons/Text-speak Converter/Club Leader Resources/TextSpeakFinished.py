def displayMenu():
    print("trdtr de exprss")
    print("=" * 13)
    print("Menu:")
    print("  c = converter uma frase")
    print("  p = imprimir dicionário")
    print("  a = adicionar uma palavra")
    print("  d = remover uma palavra")
    print("  q = sair")

#-------------------------------------------------------

def convertSentence():
    sentence = input("Insira uma frase para traduzir: ").lower()
    translatedSentence = ""

    #divide a frase em uma lista de palavras
    listOfWords = sentence.split()

    for word in listOfWords:
        #adiciona a palavra traduzida se ela existir no dicionário
        if word in textSpeakDictionary:

            translatedSentence += textSpeakDictionary[word] + " "

        #mantém a palavra original caso não exista tradução
        else:

            translatedSentence += word + " "

    #imprime a frase traduzida
    print("==>")
    print(translatedSentence)  

#-------------------------------------------------------

def addDictionaryItem():
    txtToAdd = input("Insira a expressão a ser adicionada ao dicionário: ")
    meaning = input("O que isso significa?: ")
    #adiciona a nova tradução ao dicionário
    textSpeakDictionary[txtToAdd] = meaning

#-------------------------------------------------------

def deleteDictionaryItem():
    txtToDelete = input("Insira a expressão a ser removida ao dicionário: ")
    #remove a tradução do dicionário
    del textSpeakDictionary[txtToDelete]

#-------------------------------------------------------
# o programa principal começa aqui!
#-------------------------------------------------------

textSpeakDictionary = {
    "lol"  : "laugh out loud" ,
    "idk"  : "I don't know" ,
    "jk"   : "just kidding" ,
    "bc"   : "because"
}

running = True

displayMenu()

#repete até que o usuário digite 'q' para sair
while running == True:

    menuChoice = input(">_").lower()

    #c para converter
    if menuChoice == 'c':
        convertSentence()

    #p para imprimir
    elif menuChoice == 'p':
        print(textSpeakDictionary)

    #a para adicionar
    elif menuChoice == 'a':
        addDictionaryItem()

    #d para remover
    elif menuChoice == 'd':
        deleteDictionaryItem()

    #q para sair
    elif menuChoice == 'q':
        running = False

    else:
        print("Escolha inválida!")
