textSpeakDictionary = {
    "lol"   : "laugh out loud" ,
    "idk"   : "I don't know"
}

#imprima o dicionário inteiro
print( "Dicionário =" , textSpeakDictionary )

#imprime apenas o conteúdo relacionado à chave "lol"
print( "lol =" , textSpeakDictionary["lol"] )

#texto que pede a entrada do usuário
key = input("O que você gostaria de converter? : ")
print( key , "=" , textSpeakDictionary[key] )
