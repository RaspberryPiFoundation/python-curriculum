### implementing a ceasar cipher

### nb useful to draw a clock but with a..z instead of 1..12
### to explain modulo arithmetic

alphabet = "abcdefghijklmnopqrstuvwxyz"

# can check with
# print len(alphabet), len(set(alphabet))


# convert letter to offset

# explanation about offsets, or movements. counting steps away
# like in UK lifts we have a Ground Floor.


letter = "a"
secret = 17

position = alphabet.find(letter)

newposition = (position + secret)

if newposition >= 26:
    newposition = newposition - 26

# or

newposition = newposition % 26

secretletter = alphabet[newposition]


# encryption is done

# now to reverse it, instead of adding, we subtract


secret =17
secretletter = "r"

newposition = alphabet.find(secretletter)
if newposition < 0:
    newposition = newposition + 26

letter = alphabet[newposition]


# let's make functions
"""

def encode(letter, secret):
    ....


def decode(letter, secret):
    ....

"""

def encode(letter, secret):
    pos = alphabet.find(letter)
    pos = (pos + secret)%26
    return alphabet[pos]


def decode(letter, secret):
    pos = alphabet.find(letter)
    pos = (pos + secret)%26
    return alphabet[pos]
    

## try them out

then

secret = 17
message = "hello world"

for character in message:
    if character in alphabet:
        print encode(character, secret),
    else:
        print character,


secret = 17
message = "yvccf nficu"

for character in message:
    if character in alphabet:
        print encode(character, secret),
    else:
        print character,


