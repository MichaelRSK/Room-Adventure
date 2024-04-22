#####################################
#Michael Krueger
#11/30/2022
#Room Adventure
#####################################

from Room import Room
######################################################

# creates the rooms
def createRooms():
# r1 through r4 are the four rooms in the mansion
# currentRoom is the room the player is currently in (which
# can be one of r1 through r4)
# since it needs to be changed in the main part of the
# program, it must be global
    global currentRoom
    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    # add exits to room 1
    r1.addExit("east", r2)
    r1.addExit("south", r3)
    # add grabbables to room 1
    r1.addGrabbable("key")
    # add items to room 1
    r1.addItem("chair", "It is made of Indian Wood and seems someone was just sitting on it.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")
    r1.addItem("footprints", "It looks like someone was walking east.")
    r4.addItem("treasure", "Maybe there is something good inside. Use key.")
    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    # add items to room 2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.")
    r2.addItem("person", "")
    #room 3
    r3.addItem("boardgame", "Looks like fun, but I have to keep moving so I don't get caught.")
    # set room 1 as the current room at the beginning
    # of the game
    r3.addExit("east", r4)
    r3.addExit("north", r1)
    r4.addExit("west", r3)
    r4.addExit("north", r2)
    r4.addExit("south", None)
    currentRoom = r1

        
    

        

def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$"* 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 +"u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 +"u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3+ "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" +"$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u"+ "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3+ " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9+ "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " *4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 +"u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" *2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2+ " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" +"$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" +"$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
######################################################
# START THE GAME!!!
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game

print("You are robbing a house. Try to find something to get rid of the person in the house.")
# play forever (well, at least until the player dies or asks to
#  quit)
while (True):
    if "human_head" in inventory:
        print("congrats you win")
        break
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    # if the current room is None, then the player is dead
    # this only happens if the player goes south when in room 4
    if (currentRoom == None):
        status = "You are dead."
        death()
        quit()
    if (currentRoom.name == "Room 3"):
        print("There is nothing for me to steal in here. Better keep moving.")
    # display the status
    print("=========================================")
    print(status)
        
    # if the current room is None (and the player is dead),
    #  exit the game

        

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    action = input("What to do? ")

    # set the user's input to lowercase to make it easier to
    #  compare the verb and noun to known values
    action = action.lower()

    # exit the game if the player wants to leave (supports
    #  quit, exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break

    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are go, look, take, and use"
    # split the user input into words (words are separated by
    #  spaces)
    words = action.split()

    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if (verb == "go"):
            # set a default response
            response = "Invalid exit."
            

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                # these if statements are for if room 2 is entered without a baseball bat and the person instantly dies
                if (noun == currentRoom.exits[i]):
                    if (currentRoom.name == "Room 1"):
                        if (noun == "east"):
                            if("baseball_bat" in inventory):
                                print("Uh Oh!! The owner of the house is here in room 2. Better pull out my bat")
                            else:  
                                print("Person says: Whoops, you're in the wrong house!!! You should have brought the baseball bat. Now you die!!!")
                                response = death()
                                quit()
                                
                                
                                
                    if (currentRoom.name == "Room 4"):
                        if (noun == "north"):
                            if("baseball_bat" in inventory):
                                print("\nUh Oh!! The owner of the house is here in room 2. Better pull out my bat")
                            else:                               
                                print("Person says: Whoops, you're in the wrong house!!! You should have brought the baseball bat. Now you die!!!")
                                response = death()
                                quit()
                                
                                  
                                
                    # change the current room to the one
                    #  that is associated with the specified
                    #  exit
                    currentRoom =  currentRoom.exitLocations[i]

                    # set the response (success)
                    response = "Room changed."

                    # no need to check any more exits
                    break
            
        # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."

            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if (noun == currentRoom.items[i]):
                    # set the response to the item's
                    #  description
                    #remove item from description
                    if "key" in inventory and noun == "table":
                        currentRoom.itemDescriptions[i] = "It is made of oak. It is empty."
                    response = currentRoom.itemDescriptions[i]

                    # no need to check any more items
                    break
                
        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current
            #  room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable): 
                    # add the grabbable item to the player's
                    #  inventory
                    inventory.append(grabbable)

                    # remove the grabbable item from the
                    #  room
                    currentRoom.delGrabbable(grabbable)

                    # set the response (success)
                    response = "Item grabbed."

                    # no need to check any more grabbable
                    #  items
                    break
                
                    
                
        elif (verb == "use"):
            # set a default response
            response = "I don't see that item in your inventory."
            if(noun in inventory):
                #for if the key is used you get the base ball bat
                if (noun == "key"):
                    response = "Hmmmm, there is no place to use this key. Try another room"
                    if (currentRoom.name == "Room 4"):
                        response = "Treasure has opened!!! You have recieved a Baseball Bat"
                        inventory.append("baseball_bat")
            #for using the baseball bat
            if(noun in inventory):
                if (noun == "baseball_bat"):
                    response = "There's nothing to hit in this room."
                    if (currentRoom.name == "Room 2"):
                        response = "You hit the person knocking their head off."
                        inventory.append("human_head")

                
        
        
                        
                
    # display the response
    print("\n{}".format(response))

