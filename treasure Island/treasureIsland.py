import time

def runGame():
    print("Welcome to Treasure Island!!! ")
    print("Your misson is to find the treasure ")
    
    decision = input("Left or right: ")
    if (decision.lower() == "Right".lower()):
        return "Game Over"
    elif (decision == 'Left'.lower()):
        decision = input("Swim or wait? ")
        if (decision.lower() == 'swim' ):
            return 'Game Over'
        elif (decision.lower() == 'wait'):
            time.sleep(10)
            decision = input("Which door? Red or Yellow or Blue ")
            if (decision.lower() != 'yellow'):
                return 'Game over'
            else:
                time.sleep(1)
                return 'You win!!!'
        else:
            return "Game system fail . . . . . ." 
    else:
        return "Game system fail ....... "
    

print(runGame())