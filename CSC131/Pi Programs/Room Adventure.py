###########################################################################################
# Name: Meagan Kropp
# Date: January 15, 2019
# Description: Find a key that will unlock the door to escape, but be careful of taking the wrong exit.
###########################################################################################

###########################################################################################
# the blueprint for a room
class Room(object):
        # the constructor
        def __init__(self, name):
                # rooms have a name, exits (e.g., south), exit locations (e.g., to the south is room n),
                # items (e.g., table), item descriptions (for each item), and grabbables (things that can
                # be taken into inventory)
                self.name = name
                self.exits = []
                self.exitLocations = []
                self.items = []
                self.itemDescriptions = []
                self.grabbables = []
                self.usables = []

        # getters and setters for the instance variables
        @property
        def name(self):
                return self._name

        @name.setter
        def name(self, value):
                self._name = value


        @property
        def exits(self):
                return self._exits

        @exits.setter
        def exits(self, value):
                self._exits = value

        @property
        def exitLocations(self):
                return self._exitLocations

        @exitLocations.setter
        def exitLocations(self, value):
                self._exitLocations = value

        @property
        def items(self):
                return self._items

        @items.setter
        def items(self, value):
                self._items = value

        @property
        def itemDescriptions(self):
                return self._itemDescriptions

        @itemDescriptions.setter
        def itemDescriptions(self, value):
                self._itemDescriptions = value

        @property
        def grabbables(self):
                return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
                self._grabbables = value

        @property
        def usables(self):
                return self._usables

        @usables.setter
        def usables(self, value):
                self._usables = value

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
                # append the exit and room to the appropriate lists
                self._exits.append(exit)
                self._exitLocations.append(room)

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
                # append the item and description to the appropriate lists
                self._items.append(item)
                self._itemDescriptions.append(desc)

        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
                # append the item to the list
                self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
                # remove the item from the list
                self._grabbables.remove(item)

        # show usable items in the room
        # the item is a string (e.g., door)
        def addUsable(self, item):
                # append the item to the list
                self._usables.append(item)

        # returns a string description of the room
        def __str__(self):
                # first, the room name
                s = "You are in {}.\n".format(self.name)

                # next, the items in the room
                s += "You see: "
                for item in self.items:
                        s += item + " "
                s += "\n"

                # next, the items that can be used in the room
                s += "You can use: "
                for usable in self.usables:
                        s += usable  + " "
                s += "\n"

                # next, the exits from the room
                s += "Exits: "
                for exit in self.exits:
                        s += exit + " "

                return s

###########################################################################################
# creates the rooms
def createRooms():
        # r1 through r9 are the nine rooms in the mansion
        # currentRoom is the room the player is currently in (which can be one of r1 through 9)
        # since it needs to be chnaged in the main part of the program, it must be global
        global currentRoom

        #create the rooms and give them meaningful names
        r1 = Room("Room 1")
        r2 = Room("Room 2")
        r3 = Room("Room 3")
        r4 = Room("Room 4")
        r5 = Room("Room 5")
        r6 = Room("Room 6")
        r7 = Room("Room 7")
        r8 = Room("Room 8")
        r9 = Room("Room 9")

        ### ROOM 1 ###
        # add exits to room 1
        r1.addExit("east", r2)          # -> to the east of room 1 is room 2
        r1.addExit("south", r3)
        # add grabbables to room 1
        r1.addGrabbable("key")
        # add items to room 1
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak.  A golden key rests on it.")


        ### ROOM 2 ###
        # add exits to room 2
        r2.addExit("west", r1)
        r2.addExit("south", r4)
        # add items to room 2
        r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
        r2.addItem("fireplace", "It is full of ashes.")

        ### ROOM 3 ###
        # add exits to room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        # add grabbables to room 3
        r3.addGrabbable("book")
        # add items to room 3
        r3.addItem("bookshelves", "They are empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("desk", "The stature is resting on it. So is a book.")

        ### ROOM 4 ###
        # add exits to room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", r6)
        # add grabbables to room 4
        r4.addGrabbable("6-pack")
        # add items to room 4
        r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")

        ### ROOM 5 ###
        # add exits to room 5
        r5.addExit("south", None)  # death
        # add items to room 5
        r5.addItem("sign", "It says that you made a mistake coming in here, only way out is through the window.")
        r5.addItem("window", "You look out it, you can't see the ground.")

        ### ROOM 6 ###
        # add exits to room 6
        r6.addExit("east", r7)
        r6.addExit("north", r4)
        r6.addExit("west", r5)        
        # add items to room 6
        r6.addItem("table", "It has the letters E,N,N etched on it.")

        ### ROOM 7 ###
        # add exits to room 7
        r7.addExit("west", r6)
        r7.addExit("north", r8)
        r7.addExit("south", None)  # death

        ### ROOM  8 ###
        # add exits to room 8
        r8.addExit("north", r9)
        r8.addExit("south", r7)

        ### ROOM 9 ###
        # add exits to room 9
        r9.addExit("south", r8)  
        r9.addExit("east", None) # death
        # add usables to room 9
        r9.addUsable("door")
        # add items to room 9
        r9.addItem("sign", "It says it might be easier to just die if you got here without a key.")
        

        #set room 1 as current room at the beginning of the game
        currentRoom = r1
        

# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
def death():
        print " " * 17 + "u" * 7
        print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
        print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
        print " " * 9 + "u" + "$" * 21 + "u"
        print " " * 8 + "u" + "$" * 23 + "u"
        print " " * 7 + "u" + "$" * 25 + "u"
        print " " * 7 + "u" + "$" * 25 + "u"
        print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u"
        print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\""
        print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" + "$" * 3
        print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3
        print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 + "$" * 3 + "u" * 2 + "$" * 4 + "\""
        print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7 + "\""
        print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
        print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
        print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$" * 2 + " " * 7 + "u" * 3
        print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + " " * 7 + "u" + "$" * 4
        print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 + "\"" + " " * 5 + "u" * 2 + "$" * 6
        print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 + "u" * 4 + "$" * 10
        print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\""
        print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 + " " + "\"" * 2 + "$" + "\"" * 3
        print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
        print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 + " \"\"" + "$" * 11 + "u" * 3 + "$" * 3
        print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" * 11 + "\""
        print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" * 4 + "\"\""
        print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""


def escape():
        print
        print "==================================================================================="
        print "CONGRATULATIONS!!!!!!"
        print "YOU ESCAPED AND DIDN'T DIE!!!"
        

###########################################################################################
# START THE GAME!!!
inventory = [] # nothing in inventory
createRooms() # add the rooms to the game


# play forever (well, at least until the player dies or asks to quit)
while (True):
        # set the status so the player has situational awareness
        # the status has room and inventory information
        status = "{}\nYou are carrying: {}\n".format(currentRoom,inventory)

        # if the current room is None, then the player is dead
        if (currentRoom == None):
                status = "You are dead."
        # display the status
        print "========================================================="
        print status

        # if the current room is None (and the player is dead), exit the game
        if (currentRoom == None):
                death()
                break



        # prompt for player input
        # the game supports a simple language of <verb> <noun>
        # valid verbs are go, look, take, and use
        # valid nouns depend on the verb
        # we use raw_input here to treat the input as a string instead of a numeric value
        action = raw_input("What to do? ")

        # set the user's input to lowercase to make it easier to compare the verb and noun to known values
        action = action.lower()

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye"):
                break

        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, take, and use"
        # split the user input into words (words are separated by spaces)
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
                                if (noun == currentRoom.exits[i]):
                                        # change the current room to the one that is
                                        # associated with the specified exit
                                        currentRoom = currentRoom.exitLocations[i]

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
                                        # set the response to the item's description
                                        response = currentRoom.itemDescriptions[i]

                                        # no need to check any more items
                                        break

                # the verb is: take
                elif (verb == "take"):
                        # set a default response
                        response = "I don't see that item."

                        # check for valid grabbable items in the current room
                        for grabbable in currentRoom.grabbables:
                                # a valid grabbable item is found
                                if (noun == grabbable):
                                        # add the grabbable item to the player's inventory
                                        inventory.append(grabbable)

                                        # remove the grabbable item from the room
                                        currentRoom.delGrabbable(grabbable)

                                        # set the response (success)
                                        response = "Item grabbed."

                                        # no need to check any more grabbable items
                                        break
                #the verb is: use
                elif (verb == "use"):
                        #set default response
                        response = "Nothing to use."

                        #check for valid usable items in current room
                        for usables in currentRoom.usables:
                                # a valid item is found
                                if (noun == currentRoom.usables[i]):
                                        if (usables == "door"):
                                                for i in range(len(inventory)):
                                                        if ("key" == inventory[i]):
                                                               escape()
                                                                    
                        break
                                        

                                


                
        # display the response
        print "\n{}".format(response)
