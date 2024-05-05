import os
import random
from time import sleep

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def displayScores(userHandScore:int, dealerHandScore:int):
        print(f"Your score {userHandScore}")
        sleep(3)
        print(f"Dealer's score {dealerHandScore}")

'''
The function calculateScore compares the values of 2 lists, returning the result.
returns win/lose/draw.
'''
def calculateScore(userHand: list, dealerHand: list):
    userHandScore = sum(userHand)
    dealerScore = sum(dealerHand)
    
    if userHandScore > 21 and dealerScore <= 21:
        print(f"Your score: {userHandScore}")
        return "You LOSE."
    elif userHandScore <= 21 and userHandScore > dealerScore:
        displayScores(userHandScore=userHandScore, dealerHandScore=dealerScore)
        return "You Win!"
    elif dealerScore > 21 and userHandScore <= 21:
        displayScores(userHandScore=userHandScore, dealerHandScore=dealerScore)
        return "You Win!"
    elif userHandScore < 21 and userHandScore < dealerScore:
        displayScores(userHandScore=userHandScore, dealerHandScore=dealerScore)
        return 'You LOSE.' 
    elif userHandScore == dealerScore:
        displayScores(userHandScore=userHandScore, dealerHandScore=dealerScore)
        return 'Draw!'
    else:
        displayScores(userHandScore=userHandScore, dealerHandScore=dealerScore)
        return "Dealer Wins!"
    

'''
The function blackJack simulates a game of blackJack.
Two players, the user and the CPU(dealer).
One parameter, a list representing the values held by the type of card in a deck.
returns winner/loser/draw
'''
def blackJack(cards:list):
    # First hand of 2
    userHand = random.choices(population=cards, k=2)
    dealerHand = random.choices(population=cards, k=2)
    randomDealerCard = random.choice(dealerHand)
        
    while (True):
            
        print(f"Your hand {userHand}")
        print(f"Dealer's First Cards: {randomDealerCard}")

        hitMe = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if (hitMe == 'n'):
            # Check final score
            return calculateScore(userHand=userHand, dealerHand=dealerHand)
        elif (hitMe == 'y'):
            # Hand each player a card
            userHand.append(random.choice(cards))
            dealerHand.append(random.choice(cards))
            if (sum(userHand) > 21 or sum(dealerHand) > 21):
                return calculateScore(userHand=userHand, dealerHand=dealerHand)
    

def main():
    # display logo
    print(logo)
    print("Do you want to play a game of BlackJack? Type 'y' for yes and 'n' for no: " )
    play = input().lower()
    if (play == 'y'):
        os.system('cls')
        return blackJack(cards)
    else:
        os.system('cls')
        return 0


print(main())