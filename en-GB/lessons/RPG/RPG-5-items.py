def showInstructions():
    #print a main menu and the commands
    print("RPG Game")
    print("========")
    print("Commands:")
    print("   go [direction]")
    print("   get [item]")

def showStatus():
    #print the player's current status
    print("---------------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    #print the current inventory
    print("Inventory : " + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other room positions
rooms = {

            1 : {  "name"  : "Hall" ,
                   "south" : 2 ,
                   "east"  : 4 ,
                   "item"  : "key"
                } ,        

            2 : {  "name"  : "Kitchen" ,
                   "north" : 1 ,
                   "east"  : 3
                } ,

            3 : {  "name" : "Dining Room" ,
                   "west" : 2 ,
                   "east" : 5 ,
                   "south" : 6 ,
                   "item" : "shield"
                } ,

            4 : {  "name"  : "Living Room" ,
                   "west"  : 1
                } ,

            5 : {  "name"  : "Study" ,
                   "west"  : 3
                } ,

            6 : {  "name"  : "Garden" ,
                   "north"  : 3
                }
         }

#start the player in room 1
currentRoom = 1

showInstructions()

#loop infinitely
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = input(">").lower().split()

    #if they type 'go' first
    if move[0] == "go":
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print("You can't go that way!")

    #if they type 'get' first
    if move[0] == "get" :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + " got!")
            #delete the item from the room
            del rooms[currentRoom]["item"]
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print("Can't get " + move[1] + "!")
