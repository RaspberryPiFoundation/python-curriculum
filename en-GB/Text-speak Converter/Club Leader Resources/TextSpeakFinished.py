def displayMenu():
    print("txt spk cnvtr")
    print("=" * 13)
    print("Menu:")
    print("  c = convert a sentence")
    print("  p = print dictionary")
    print("  a = add a word")
    print("  d = delete a word")
    print("  q = quit")

#-------------------------------------------------------

def convertSentence():
    sentence = input("Enter a sentence to translate: ").lower()
    translatedSentence = ""

    #this splits up the sentence into a list of words
    listOfWords = sentence.split()

    for word in listOfWords:
        #add the translated word if it exists in the dictionary
        if word in textSpeakDictionary:

            translatedSentence += textSpeakDictionary[word] + " "

        #just keep the original word if there's no translation
        else:

            translatedSentence += word + " "

    #print the translated sentence
    print("==>")
    print(translatedSentence)  

#-------------------------------------------------------

def addDictionaryItem():
    txtToAdd = input("Enter the text-speak to add to the dictionary: ")
    meaning = input("What does this mean?: ")
    #add the new translation to the dictionary
    textSpeakDictionary[txtToAdd] = meaning

#-------------------------------------------------------

def deleteDictionaryItem():
    txtToDelete = input("Enter the text-speak to delete from the dictionary: ")
    #delete the translation from the dictionary
    del textSpeakDictionary[txtToDelete]

#-------------------------------------------------------
# main program starts here!
#-------------------------------------------------------

textSpeakDictionary = {
    "lol"  : "laugh out loud" ,
    "idk"  : "I don't know" ,
    "jk"   : "just kidding" ,
    "bc"   : "because"
}

running = True

displayMenu()

#repeat until the user inputs 'q' to quit
while running == True:

    menuChoice = input(">_").lower()

    #c to convert
    if menuChoice == 'c':
        convertSentence()

    #p to print
    elif menuChoice == 'p':
        print(textSpeakDictionary)

    #a to add
    elif menuChoice == 'a':
        addDictionaryItem()

    #d to delete
    elif menuChoice == 'd':
        deleteDictionaryItem()

    #q to quit
    elif menuChoice == 'q':
        running = False

    else:
        print("Invalid menu choice!")
