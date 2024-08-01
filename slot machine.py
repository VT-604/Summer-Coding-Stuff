#VT-604
#7/29
#Slot Machine
#Initial
import random
slot=['♥', '♦', '♠', '♣', '☆', '7', '§']
#Functions
def slotMachine():
    balance=100
    bet=10
    print("-------{Welcome to Fazzy's Gambling Den}-------\n\nSlot Machine Symbols: ♥, ♦, ♠, ♣, ☆, 7\n\nEach spin costs 10 credits, but you can bet higher for more rewards. \n")
    while True:
        if balance >=10:
            balance=str(balance)
            print("Your total balance is "+balance+" credits\n\nPress 'S' to spin, 'B' to change bets, and 'Q' to quit\n")
            balance=int(balance)
            bet=int(bet)
            option=input("Option: ")
            if option=="S" and balance>=10:
                balance=balance-bet
                result1=random.choices(slot, weights=[1,1,1,1,1,0.75,0.01])
                result2=random.choices(slot, weights=[1,1,1,1,1,0.75,0.01])
                result3=random.choices(slot, weights=[1,1,1,1,1,0.75,0.01])
                print("You chose: "+option+"\n\nSpinning...\n\n["+result1[0]+"]"+" ["+result2[0]+"] ["+result3[0]+"]\n")
                if result1[0]=="§" and result2[0]=="§" and result3[0]=="§":
                    print("You found the secret symbol. Well done. Even I didn't think it was possible.\n")
                    balance=balance+bet*1000000
                elif result1[0]=="7" and result2[0]=="7" and result3[0]=="7":
                    print("YOU HIT A JACKPOT!!!\n")
                    balance=balance+bet*50
                elif result1[0]=="♥" and result2[0]=="♥" and result3[0]=="♥":
                    print("You won!\n")
                    balance=balance+bet*5
                elif result1[0]=="♦" and result2[0]=="♦" and result3[0]=="♦":
                    print("You won!\n")
                    balance=balance+bet*5
                elif result1[0]=="♠" and result2[0]=="♠" and result3[0]=="♠":
                    print("You won!\n")
                    balance=balance+bet*5
                elif result1[0]=="♣" and result2[0]=="♣" and result3[0]=="♣":
                    print("You won!\n")
                    balance=balance+bet*5
                elif result1[0]=="☆" and result2[0]=="☆" and result3[0]=="☆":
                    print("You won!\n")
                    balance=balance+bet*5
                else:
                    print("You lost...\n")
            elif option=="Q" and balance>=10:
                print("You chose: "+option+"\n\nAre you sure? You could make much more money! Y/N\n")
                tempt=input("Option: ")
                if tempt=="Y":
                    print("You chose: "+tempt+"\n\nFine. You can leave knowing you could've made much more money.\n")
                    break
                elif tempt=="N":
                    print("You chose: "+tempt+"\n\nGreat choice! You're a finacially responsible oppurtunist!\n")
                else:
                    print("I didn't quite understand that, so I'm going to assume that you want to gamble some more!")
                break
            elif option=="B":
                print("How many credits would you like to bet per spin?\n")
                bet=int(input("Amount: "))
            else:
                print("I didn't quite understand that, so I assume that you're going to spin.\n")
        elif balance<=9:
            print("You're out of credits. Get out. \n")
            break
#Main
slotMachine()
