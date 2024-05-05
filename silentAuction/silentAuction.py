import os

def getLogo():
    logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
    '''
    return logo

def silentAuction():
    print(getLogo())
    run = True
    bidders = dict()
    while run:
        name = input("What is your name?: ")
        bid = float(input("What is your bid?: "))
        bidders[name] = bid
        moreBidders = input("Are there any other bidders? Type 'yes' or 'no': ")
        if moreBidders.lower() == 'no':
            run = False
        elif moreBidders.lower() == 'yes':
            os.system('cls')

    winner_name = max(bidders, key=bidders.get)
    winner_bid = bidders[winner_name]
    return f"The winner is {winner_name} with a bid of R{winner_bid}."

        

def main():
     return silentAuction()
    
print(main())