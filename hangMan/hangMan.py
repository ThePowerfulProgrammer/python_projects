import random

# randomWord = ""
# with open("commonWords.txt") as rFile:
#     words = rFile.readlines()
#     randomWord = random.choice(words)
    
# print(f"The mystery word is {randomWord}")

# hiddenWord = []
# for _ in range(len(randomWord) - 1):
#     hiddenWord += "_"

# print(f"{'_'*(len(randomWord) - 1) }")
    
# guess = input("Guess a character in the mystery word: ").lower()

# for pos in range(len(randomWord) - 1):
#     if randomWord[pos] == guess:
#         hiddenWord[pos] = guess

# print(hiddenWord) 
    
    
def generateHiddenWord():
    randomWord = ""
    with open("commonWords.txt") as rFile:
        words = rFile.readlines()
        randomWord = random.choice(words)
        
    return randomWord

def beginGame(randomWord: str):
    print("Hello, let's play hangman :^) ")
    print(randomWord)
    lenRandomWord = len(randomWord)-1
    userLives = random.randint(lenRandomWord, lenRandomWord+3)
    
    print(f"The hidden word is {'_'*lenRandomWord}")    
    
    hiddenWord = []
    for _ in range(lenRandomWord):
        hiddenWord += '_'
        
    while (userLives > 0 and '_' in hiddenWord):
        guess = input("Take a guess: ")
                
        if guess in randomWord:
            for pos in range(lenRandomWord):
                if randomWord[pos] == guess:
                    hiddenWord[pos] = guess
            print(''.join(hiddenWord))
        else:
            print("Wrong guess, try again")
            userLives -= 1
            print(''.join(hiddenWord))
            
    if (userLives == 0):
        print("You lost!!! ")
        return "Lost."
    else:
        print(f"Congrats, the hidden word was {''.join(hiddenWord)}")
        return "Win!!!"        


print(beginGame(generateHiddenWord()))    
