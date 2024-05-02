import random 

def tossCoin():
    if (random.randint(0,1) == 0):
        return 'Tails'
    return 'Heads'

print(tossCoin())
print(tossCoin())
print(tossCoin())