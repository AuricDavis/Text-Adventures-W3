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