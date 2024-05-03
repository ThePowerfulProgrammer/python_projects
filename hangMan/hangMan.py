import random

# Step 1) Create game --> greetings, choose random word, set user lives, display word hidden, keep track of correct user guesses
# Step 2) Begin playing game --> User is told about lives, and guessing begins.
#     Step 2a) User guess --> User makes a correct decision, insert correct letten to reveal portion of hidden word
#     Step 2b) User guess --> USer makes an incorrect decision, print warning, reduce lives
# Step 3) Game over
#     Step 3a) User wins --> Word has been guessed and lives != 0
#     Step 3b) User loses --> Word has not being guessed and lives == 0  


# generate random word
def generateRandomWord() -> str:
    word = ""
    with open("commonWords.txt") as rFile:
        words =  rFile.readlines()
        word = random.choice(words)
    return word

# helper 
def printWord(word, guessed):
    for c in word:
        if c in guessed:
            print(c, end='')
        else:
            print("_", end="")
    return "\n"



# Step 2
def beginGame(word: str,lives: int, letterGuessed: list):
    win = False   
    hiddenWord = "_"*len(word)
    
    while (lives > 0 and win == False):
        userGuess = input("Take a guess: ")
        
        if (userGuess in word):
            letterGuessed.append(userGuess)
            printWord(word, letterGuessed)
            if (len(letterGuessed) == len(word)):
                win = True
        else:
            print(f"Wrong guess, you have {lives-1} guesses remaining")
            printWord(word, letterGuessed)
            lives -= 1
            
    if (win):
        return True
    else:
        return False        
                    
        
    
    

# Step 1
def createGame():
    randomWord = generateRandomWord()

    userLives = random.randint(len(randomWord),len(randomWord) + 3)
    
    lettersGuessed = [] # Keep track of correct user guesses
    
    print(f"We are going to play hangman, you have {userLives} guesses")
    print(f"Hidden word: ")
    print(randomWord)
    print('_'*len(randomWord))
    
    win_or_lose =  beginGame(randomWord, userLives, lettersGuessed)
    
    if (win_or_lose):
        return "You win congrats"

    print(f"The word was {randomWord}")
    return "You lost, loser!!!"
    
print(createGame())
    
    
    
    
     