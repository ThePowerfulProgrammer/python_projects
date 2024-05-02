
def charInString(name, stringCheck):
    sum = 0
    for c in name:
        if c.lower() in stringCheck.lower():
            sum += 1
            
    return sum

def loveCalculator():
    print("The love calculator is calulating your score ...")
    name1 = input("What is your name? ")
    name2 = input("What is your partner's name? ")
    
    loveScore = 0
    
    loveScore += (charInString(name1, 'true') + charInString(name2, 'true')) * 10
    loveScore += charInString(name1,'love') + charInString(name2, 'love')
    
    
    if (loveScore < 10 or loveScore > 90):
        print(f"Your score if {loveScore}, your love goes together like coke and mentos")
    elif (loveScore >= 40 and loveScore <= 50):
        print(f"Your score is {loveScore}, you are alright together")
    else:
        print(f"Your score is {loveScore}")
        
    return None
    
            
loveCalculator()

        