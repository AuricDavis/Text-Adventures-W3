print("To start the game, type \"start\".\nTo quit the game, type \"quit\"")
fromUser = input()
while True:
    if fromUser == "start":
        print("Get ready for your adventure!")
        
    elif fromUser == "quit":
        print("Okay, I wanted to be alone anyway!")
        break
    elif fromUser.split()[0] == "go":
        print("Go where? I need instructions!")
    else:
        print("... You're not very bright, are you? \nTo start the game, type \"start\"")
    fromUser = input()

# Variables
START_X = 0
START_Y = 0
MAP_X = 4
MAP_Y = 8

x = START_X
y = START_Y

# Commands
def go(direction):
    global x 
    global y 
    if direction == 'north':
        if (y + 1) >= MAP_Y:
            print("There's a wall there")
        else:
            y += 1
            print("Went north")
    if direction == "south":
        if (y - 1) <= MAP_Y:
            print("There's a wall there")
        else:
            y -= 1
            print("Went south")
    if direction == "east":
        if (x + 1) >= MAP_X:
            print("There's a wall there")
        else:
            x += 1
            print("Went east")
    if direction == "west":
        if (x - 1) <= MAP_X:
            print("There's a wall there")
        else:
            x -= 1
            print("Went west")

    else:
        print("I don't understand which direction you're trying to go")

while True:
    # Print out all the stuff related to the room

    # Get input from the user
    fromUser = input()
    if fromUser == "quit":
        print("Game over!")
        break
    elif fromUser.split()[0] == "go":
        go(fromUser.split()[1])
    else:
        print("That didn't make any sense to me")