
### STORY GAME ### (again)


# Initial Situation
print("""
Alright, that last tequila was probably one too many.

You just woke up in some sort of cave, you cant see anything and its cold.
Your pockets are mostly empty, the only thing you got is a flashlight - no phone though.
""")


#level1 (done in class)
level1_done = False

while level1_done == False:
    print("What do you do? (LOOK/SHOUT/MOVE)")
    choice = input() #taking input from player
    if choice == "LOOK":
        print("You look around, but its too dark to see")
        print("USE FLASHLIGHT? (Y/N)")
        sub_choice = input()
        if sub_choice == "Y":
            print("Its broken!!")
        else:
            print("man you really cant see anything")
    elif choice == "SHOUT":
        print("You shout from the top of your lungs - but no one replies.")
    elif choice == "MOVE":
        print("You just move without seeing - but you feel there is a door in front of you!")
        level1_done = True
    else:
        print("Your input is invalid.")
print()
print("Level 1 Complete")


#level2 (done on my own)
level2_done = False

# New Situation
print("""
On the other side of the door you find the entrance of the cave. Now your outside but it dark
it looks like your on a steep rocky mountain with trees around you.
""")

while level2_done == False:
    print("Now What!! Wait till morning or Move (WAIT/MOVE)")
    choice = input() #taking input form player
    if choice == "WAIT":
        print("A wolf come and attacks you and you died!!!")
    elif choice == "MOVE":
        print("Would you like to go up or down (UP/DOWN)")
        sub_choice = input()
        if sub_choice == "UP":
            print("""You climb your way up the Mt and reach the top where you find a
little hut connected to a path""")
            level2_done = True
            print("Game Completed")
        else:
            print("You struggle down the Mt and find a huge cliff over a river")
    else:
        print("Your input is invalid.")