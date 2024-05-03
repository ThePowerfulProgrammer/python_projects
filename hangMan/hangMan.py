import random

randomWord = ""
with open("commonWords.txt") as rFile:
    words = rFile.readlines()
    randomWord = random.choice(words)
    
print(f"The mystery word is {randomWord}")

hiddenWord = []
for _ in range(len(randomWord) - 1):
    hiddenWord += "_"

print(f"{'_'*(len(randomWord) - 1) }")
    
guess = input("Guess a character in the mystery word: ").lower()

for pos in range(len(randomWord) - 1):
    if randomWord[pos] == guess:
        hiddenWord[pos] = guess

print(hiddenWord) 
    