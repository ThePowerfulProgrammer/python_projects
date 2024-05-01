import random
'''
Yummy app MVP 
v0.1 
The purpose of YUMMY is to produce a dinner munei from a users favourite dishes 
and produce a shopping list of ingridients if required.
'''

#  -------------- B) Lists -----------------

foodWeLike = ['chicken tikka pizza', 'chicken Burger', 'Fish and chips', 'Pancakes', 'Scrambled Eggs', 'Pasta', 'Wrap']

pizzaIngridients = ['Pizza dough', 'sauce', 'cheese', 'protein']
burgerIngridients = ['Bun', 'Chicken patty', 'lettuce', 'onion', 'chilli mayo', 'gerkins']
fishAndChipsIngridients = ['Hake battered', 'potato', 'sauce', 'salt', 'pepper']
pancakesIngridients = ['pancake dough', 'ice-cream', 'honey']
scrambledEggsIngridients = ['eggs', 'salt', 'pepper', 'sauce', 'oil']
pastaIngridients = ['pasta', 'sauce']
wrapIngridients = ['Wrap', 'Filling of choice']

dishAndIngridients = {'chicken tikka pizza':pizzaIngridients, 
                      'chicken Burger':burgerIngridients,
                      'Fish and chips':fishAndChipsIngridients, 
                      'Pancakes':pancakesIngridients, 
                      'Scrambled Eggs': scrambledEggsIngridients, 
                      'Pasta':pastaIngridients,
                      'Wrap':wrapIngridients
                      }

# 1) How many days to plan for?
print("I am !YUMMY, I will help you plan your dinner menu ... ")
def chooseDays() -> int:
    days = input("How many days would you like me to plan for in one week? : ")
    print()
    while ( days == "" or int(days) > 7 or int (days) < 1):
        print(f"Error encounted, it appears that you choose {days} days.")
        print("I can only play for 1 day minimum and 7 days max, enter a new answer please: ")
        print()
        days = input("How many days would you like me to plan for in one week? ")
        

    print()
    print(f"Alrighty, I will plan for {days} days and create {days} dinner(s) :^) ")
    return days


# 2) Choose dishes --> Function 
# Return a list containing dinners for the amount of days
def chooseDishes(days:int) -> list:
        myMenu = []
        dish = random.choice(foodWeLike)
        
        while (len(myMenu) < days):
                
            while (dish in myMenu):
                dish = random.choice(foodWeLike)

            myMenu.append(dish)
        return myMenu

def displayMenu(menu:list) -> None:
    for dish in menu:
        print(dish + " ")
    return None

# 3) Build shopping list -> ingridients list

def buildShoppingList(menu:list) -> list:
    answer = input("Would you like a shopping list? Type Yes or No: ")
    while (answer != "Yes" and answer != "No"):
            answer = input("Would you like a shopping list? Type Yes or No: ")
            
    if (answer == "No"):
        print("Okay, goodluck with cooking :^) ")
        return None

    shoppingList = []
    for dish in menu:
        if dish in dishAndIngridients.keys():
            shoppingList.append(dishAndIngridients[dish])
            
    return shoppingList

            
days = chooseDays();

menu = chooseDishes(int(days));

displayMenu(menu);
    
shoppingList = buildShoppingList(menu)

for i in shoppingList:
    print(i)