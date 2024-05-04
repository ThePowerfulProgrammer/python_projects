import random
from hangManArt import logo
from hangManArt import stages

 
# choose a random word from a txt file
def generateHiddenWord():
    randomWord = ""
    with open("commonWords.txt") as rFile:
        words = rFile.readlines()
        randomWord = random.choice(words).strip()
        
    return randomWord

def beginGame(randomWord: str):
    currentStage = 6 # reflects where our stickman is in his execution 
    showWord = int(input("Select 1 to display partial word and 0 to play on hard word: "))
    if (showWord == 1):
        print("".join(random.sample(randomWord, 2)))
    
    
    lenRandomWord = len(randomWord) # for later use grab the length of word
    userLives = random.randint(lenRandomWord, lenRandomWord+3) # worse cause user needs as many chances to guess as there are characters in word
    
    print(f"The hidden word is {'_'*lenRandomWord}")    
    print(f"You have {userLives} guesses remaining")
    
    # populate list with _ as word so far is unguessed
    hiddenWord = ['_' for _ in range(lenRandomWord)]
        
    # while user has guesses and the presence of _ indicates that the word has not been guessed completely 
    while (userLives > 0 and '_' in hiddenWord):
        guess = input("Take a guess: ")
                
        if guess in randomWord:
            for pos in range(lenRandomWord):
                if randomWord[pos] == guess:
                    hiddenWord[pos] = guess # update hidden word to reflect correct user guess
                    
            print(''.join(hiddenWord))
        else:
            print("Wrong guess, try again")
            print(stages[currentStage])
            userLives -= 1
            print(''.join(hiddenWord))
            
    if (userLives == 0):
        print("You lost!!! ")
        print(f"The word was {randomWord}")
        return "Lost."
    else:
        print(f"Congrats, the hidden word was {''.join(hiddenWord)}")
        return "Win!!!"        

print(logo)
print("Hello, let's play hangman :^) ")
print(beginGame(generateHiddenWord()))    
