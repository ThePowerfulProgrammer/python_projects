import random
import hangman


# step 1) Seed the initial word and set the game layout
def createHangMan():
    word = ''
    
    with open('words.txt') as rFile:
        words = rFile.readlines()
        word = random.choice(words)

    print(f"Your word has been chosen, it is of lenght {len(word)}")
    print(f"Your objective is to guess all letters of word and fill in {'_'*len(word)}")    

createHangMan()