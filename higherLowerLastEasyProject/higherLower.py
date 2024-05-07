from art import logo,vs
from game_data import data
import random

'''
Simulate Game Play:
Logo
Compare A: Name, desc, from Country

vs logo

Against B: Name, desc, from Country
Who has more followers? Type 'A' or 'B': 

If user gets the answer right:
    B now becomes A and we refresh B
if user gets the answer wrong:
    User loses and we return users score
'''

'''
print logo
grab random object from data call it A

print vs logo
grab random object from data call it B, ensure it is not A
user input 

if user correctly guesses:
    Switch A with B and create a new B
    increment score 
else:
    return score

'''

def checkAandB(A:dict, B:dict):
    return A == B

def playGame():
    userScore = 0
    dataSetA = random.choice(data)
    dataSetB = random.choice(data)
    
    
    while (checkAandB(dataSetA, dataSetB)): 
        dataSetB = random.choice(data)
        
    play = True
    while (play):
        print(f"Compare A: {dataSetA['name']}, {dataSetA['description']}, from {dataSetA['country']}")
        print(vs)
        print(f"Against B: {dataSetB['name']}, {dataSetB['description']}, from {dataSetB['country']}")
        
        userGuess = input("Who has more followers? Type 'A' or 'B': ")
        
        if (dataSetA['follower_count'] > dataSetB['follower_count'] and userGuess == 'A'):
            userScore += 1
        elif (dataSetA['follower_count'] < dataSetB['follower_count'] and userGuess == 'B'):
            userScore += 1
            dataSetA = dataSetB
            dataSetB = data[random.randrange(0,len(data))]
        
            while (checkAandB(dataSetA, dataSetB)): 
                dataSetB = data[random.randrange(0,len(data))]
            print(dataSetB['name'])
                
        elif (dataSetA['follower_count'] > dataSetB['follower_count'] and userGuess == 'B'):
            play = False
            return f"Ohh, Soo close: A: {dataSetA['follower_count'] * 1000000} > B: {dataSetB['follower_count'] * 1000000} \n Your end score is {userScore}"
        elif (dataSetA['follower_count'] < dataSetB['follower_count'] and userGuess == 'A'):
            play = False
            return f"Ohh, Soo close: A: {dataSetA['follower_count'] * 1000000} < B: {dataSetB['follower_count'] * 1000000} \n Your end score is {userScore}"
        
        
# Play game
def main():
    print(logo)
    
    return playGame()

print(main())