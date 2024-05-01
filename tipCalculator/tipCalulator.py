

def calculateTip():
    print("Welcome to the tip calculator")
    total_bill = float(input("How much was the total Bill? R"))
    tip = float(input("How much would you like to tip 10, 15 or 20 %"))
    while (tip < float(10.0) or tip > float(20.0)):
        tip = float(input("How much would you like to tip 10, 15 or 20 %"))
        
    split_bill = int(input("How many people is the bill being split against? "))
    
    return f'Each person should pay R{(total_bill + (total_bill * tip / 100)) / split_bill}'

print(calculateTip())