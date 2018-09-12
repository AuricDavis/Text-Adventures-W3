print("To start the game, type \"start\".\nTo quit the game, type \"quit\"")
fromUser = input()
while True:
    if fromUser == "start":
        print("Get ready for your adventure!")
        
    elif fromUser == "quit":
        print("Okay, I wanted to be alone anyway!")
        break
    else:
        print("... You're not very bright, are you?")
    fromUser = input()