#a list of the letters to encrypt
alphabet = "abcdefghijklmnopqrstuvwxyz"

#the secret key is 3
key = 3

character = input("Please enter a character to encrypt: ")

#find the position of the character in the alphabet
#e.g. 'a' is position 0, 'e' is position 4, etc.
position = alphabet.find(character)

#add the secret key to find the encrypted character position
# % 26 means 'go back to 0 once you get to 26'
newPosition = (position + key) % 26

#the encrypted letter is in the alphabet at newPosition
encryptedLetter = alphabet[newPosition]
        
print("Your encrypted letter is" , encryptedLetter)
