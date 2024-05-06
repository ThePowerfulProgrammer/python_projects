'''
To-do 
Implement in python a console based program that simulates a number guessing game between the user and the Computer.
There will be 2 modes of Play: Easy (10 guesses) and Hard (5 guesses)

At the start of the game:
    We display a message, maybe a logo
    We generate a random int using random between 1 - 100
    We state that the computer is thinking of a number between 1 and 100.
    We Allow the user to choose Easy or Hard. --> The only difference is the number of guesses.
    
    We display number of guesses the user has left.
    Begin Guessing 
    While (guesses != 0 or userGuess != randomNumber):
        if (userGuess > randomNumber):
            Too High
        elif (userGuess < randomNumber):
            Too low
    
    if (guesses == 0):
        User Lost
    if (userGuess == randomNumber):
        User Win
        
'''

import random
import os


logo = """
$$\   $$\                         $$\                                  $$$$$$\                                          
$$$\  $$ |                        $$ |                                $$  __$$\                                         
$$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\ 
$$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|
$$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  
$$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ 
$$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            \$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |
\__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|             \______/  \______/  \_______|\_______/ \_______/                                  
"""

# This is redundant 
def generateRandomNumber(lowerBound:int, upperBound:int) -> int :
    randomNumber = random.randint(lowerBound, upperBound)
    return randomNumber

def evaluate_guess(userGuess, randomNumber):
    if userGuess > randomNumber:
        return "Too high. '\n' Guess Again."
    elif userGuess < randomNumber:
        return "Too low '\n' Guess Again."




def main():
    print(logo)
    
    print("Welcome to the Number Guessing Game! ")
    
    randomNumber = generateRandomNumber(1,100)
    
    print("I'm thinking of a number between 1 and 100")
    
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard' ").lower()
    
    if (difficulty not in ('easy', 'hard') ):
        return "Error, game end"
    
    guessesLeft = 0
    if (difficulty == 'easy'):
        guessesLeft = 10
    else:
        guessesLeft = 5
    
    userGuess = 0
    while (guessesLeft > 0 and userGuess != randomNumber):
        print(f"You have {guessesLeft} attempts remaining to guess the number.")
        userGuess = int(input("Make a guess: "))

        if not isinstance(userGuess, int):
            return 'Exit'
        
        # Make this a function
        if (userGuess > randomNumber):
            print("Too high.")
            print("Guess Again.")
            guessesLeft -= 1
        elif (userGuess < randomNumber):
            print("Too low")
            print("Guess Again.")
            guessesLeft -= 1
            
        
    if (guessesLeft == 0):
        os.system('cls')
        return f"You lost the number was {randomNumber}"
    elif (userGuess == randomNumber):
        os.system('cls')
        return f"You WON!!!"

        
print(main())

