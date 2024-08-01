#VT-604
#7/30
#Roulette
#Initial
import random
import time
pockets=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
balance=100
bet=10
#Functions
def spinRouletteTable():
    global balance
    global bet
    print("-------{Welcome to Fazzy's Gambling Den}-------\n\nRoulette Pockets: 0-36. \n\nEach spin costs 10 credits, but you can bet higher for more rewards. \n\nWhat is your name? \n")
    name=input("Name: ")
    print("Welcome, "+name+". ")
    while True:
        print("What would you like to do next?\n\n1. Place a Bet \n2. Change Bet Amount\n3. Check Credits \n4. Quit \n")
        option=input("Option: ")
        if option=="1" and balance>=bet:
            print("Choose your bet type: \n\n1. Specific Number (35:1) \n2. Red or Black (1:1) \n")
            type=input("Type of Bet: ")
            if type=="1":
                print("Which number would you like to pick? \n")
                specNum=int(input("Number: "))
                if specNum>36 or specNum<0:
                    print("I apologize, dear patron, we don't have any pockets with that number. \n")
                else:
                    balance=balance-bet
                    print("Spinning... \n")
                    time.sleep(2)
                    outcome=random.choice(pockets)
                    if specNum==outcome==0:
                        winnings=bet*17
                        winnings=str(winnings)
                        print("Congratulations, you won "+winnings+" credits! \n")
                        balance=balance+(bet*17)
                    elif specNum==outcome:
                        winnings=bet*35
                        winnings=str(winnings)
                        print("Congratulations, you won "+winnings+" credits! \n")
                        balance=balance+(bet*35)
                    else:
                        outcome=str(outcome)
                        print("I apologize, but you lost. The correct answer was "+outcome+"\n")
                        outcome=int(outcome)
            elif type=="2":
                print("Would you like to pick Red or Black? \n\n1. Red\n2. Black \n\n")
                color=input("Type of Color: ")
                if color=="1":
                    balance=balance-bet
                    print("Spinning... \n")
                    time.sleep(2)
                    outcome=random.choice(pockets)
                    if outcome%2==0:
                        winnings=bet*2
                        winnings=str(winnings)
                        print("Congratulations, you won "+winnings+" credits! \n")
                        balance=balance+(bet*2)
                    elif outcome%2==1:
                        outcome=str(outcome)
                        print("I apologize, but you lost. It landed on "+outcome+", meaning it was black. \n")
                        outcome=int(outcome)
                elif color=="2":
                    balance=balance-bet
                    print("Spinning... \n")
                    time.sleep(2)
                    outcome=random.choice(pockets)
                    if outcome%2==1:
                        winnings=bet*2
                        winnings=str(winnings)
                        print("Congratulations, you won "+winnings+" credits! \n")
                        balance=balance+(bet*2)
                    elif outcome%2==0:
                        outcome=str(outcome)
                        print("I apologize, but you lost. It landed on "+outcome+", meaning it was red. \n")
                        outcome=int(outcome)
                else:
                    print("I apologize, dear patron. That is not a valid option. \n")
            else:
                print("I apologize, dear patron. That is not a valid option. \n")
        elif option=="1" and balance<bet:
            print("I apologize, dear patron, but you do not have enough credits for that bet. \n")
        elif option=="2":
            print("How many credits would you like to bet per spin?\n")
            bet=int(input("Amount: "))
            if bet<=9:
                print("I apologize, dear patron, but you cannot make a bet lower than 10 credits. \n")
                bet=10
        elif option=="3":
            balance=str(balance)
            print("Total balance is currently: "+balance+ " credits. \n")
            balance=int(balance)
        elif option=="4":
            balance=str(balance)
            print("Goodbye, "+name+" and thank you for your patronage. \nYour total balance comes out to "+balance+" credits. \n")
            balance=int(balance)
            time.sleep(5)
            break
        else:
            print("I apologize, dear patron. That is not a valid option. \n")
#Main
spinRouletteTable()
