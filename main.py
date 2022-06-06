
from rpginfo import RPGInfo
from character import Character, Enemy, Friend
from room import Room
from item import Item
from random import choice



                                                                # intro

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()




                                                                # Rooms
kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room buzzing with flies"

ballroom = Room("ballroom")
ballroom.description  = "A vast room with a shining floor." + "\n"
ballroom.description += "There's a large door to the south. (It's locked.)"

dining_hall = Room("dining hall")
dining_hall.description  = "A long room with a high ceiling, "
dining_hall.description += "but the table and chairs are missing."

outdoors = Room("outdoors")
outdoors.description = "Outside of the grand front door of the castle."

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


                                                                # Items
sword = Item("a sword")
sword.description = "The blade is blackened and blunt."
kitchen.contents.append(sword)

key = Item("a key")
key.description = "A tiny silver key on a large silky tassel." 

biscuit = Item("a biscuit")
biscuit.description = "Round, crisp, smelling of ginger."

cheese = Item("some cheese")
cheese.description = "Tasty cheddar cheese"
kitchen.contents.append(cheese)


                                                                # Characters
dave = Enemy("Dave", "A smelly zombie")
dave.conversation = "Brrlgrh... rgrhl... brains..."
dave.weakness = "cheese"
dave.owns = biscuit
dining_hall.character = dave

alys = Enemy("Alys", "A skeleton with glowing blue eyes")
alys.conversation = "I'm going to destroy you."
alys.weakness = "sword"
outdoors.character = alys

holly = Friend("Holly", "A small fluffy dog.")
holly.conversation = "<Holly wags her tail and barks.>"
holly.likes = "biscuit"
holly.owns = key
ballroom.character = holly




                                                                # initialise game
current_room = kitchen
backpack = []
dead = False
game_won = False




                                                                # start game loop
while not dead and not game_won:
    print("\n")
    inhabitant = current_room.character
    current_room.display_details()



    if len(backpack) > 0:
        print("You are carrying: " + ", ".join(backpack))
    command = input("> ").lower()
 
 
 
    if command in ["talk", "rob", "fight", "give"] and inhabitant == None:
        print("There's no-one here")
        continue



    if command in ["north", "n", "south", "s", "east", "e", "west", "w"]:
        current_room = current_room.move(command)



    elif command == "talk":
        inhabitant.talk()
        if inhabitant == dave:
            dave.conversation = choice(["Aaargh!", "Waaagh!", "Braaains!",
                                        "Brrlgrh... rgrhl... brains..."])
            
            
    elif command == "rob":
        stolen_item = inhabitant.rob()
        if stolen_item is not None:
            backpack.append(stolen_item.name)
        
        
        
    elif command == "fight":
        fight_with = input("What will you fight with? ")
        
        if fight_with not in backpack:
            print("You haven't got that.")
            continue
        
        fight_won = inhabitant.fight(fight_with)
        if fight_won and isinstance(inhabitant, Enemy):
            Character.enemies_defeated.add(inhabitant)
            if len(Character.enemies_defeated) == 2:
                print()
                print("Victory is yours, game over.")
                game_won = True
        if not fight_won:
            print("Game over")
            dead = True
        
        
        
    elif command == "give":
        gift = input("What do you want to give " + inhabitant.name + "? " )
        
        if gift not in backpack:
            print("You haven't got that.")
            continue
        
        liked = inhabitant.give(gift)     # inhabitant.owns not updated in this line
        
        if liked:
            backpack.remove(gift)
            
            if inhabitant.owns is not None:
                # characters only own one thing at a time, so may drop an item
                current_room.contents.append(inhabitant.owns)
                
            if inhabitant is holly:
                print("She runs off with the treat, leaving the key behind.")
                current_room.character = None
        
            inhabitant.owns = Item.all_Items[gift]


        
    elif command in ["get", "take"]:
        chosen = input("What do you want to " + command + "? ")
        
        # find an existing Item object matching the inputted text
        if chosen in Item.all_Items:
            chosen_Item = Item.all_Items[chosen]
        else:
            print("Huh?")
            continue
        
        # if the item is in a character's possession, print an objection
        if inhabitant is not None and inhabitant.owns == chosen_Item:
            print(inhabitant.name + " likes to keep it.")
        
        # if the item is in the room, take it, else print an objection
        else:
            if chosen_Item in current_room.contents:
                current_room.contents.remove(chosen_Item)
                backpack.append(chosen)
                if chosen == "key":
                    print("You try the key in the large door, and it opens.")
                    ballroom.description = "A vast room with a shining floor. " + "\n" + \
                                           "The large door to the south stands open."
                    ballroom.link_room(outdoors, "south")
                    outdoors.link_room(ballroom, "north")
            else:
                print("It's not here.")
        
        
        
    elif command == "drop":
        chosen = input("What do you want to drop? ")
        
        if chosen in backpack:
            backpack.remove(chosen)
            chosen_Item = Item.all_Items[chosen]
            current_room.contents.append(chosen_Item)
        else:
            print("You haven't got that.")




                                                                # credits
RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()