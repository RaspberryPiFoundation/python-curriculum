textSpeakDictionary = {
    "lol"   : "laugh out loud" ,
    "idk"   : "I don't know"
}

#print the entire dictionary
print( "Dictionary =" , textSpeakDictionary )

#print just the entry for "lol"
print( "lol =" , textSpeakDictionary["lol"] )

#ask for the key to find the entry for
key = input("What would you like to translate? : ")
print( key , "=" , textSpeakDictionary[key] )
