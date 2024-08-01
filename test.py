#VT-604
#7/30
#Test Interview
#Initial
import random
HoT=["Heads", "Tails"]
#Function
def coinFlipSimulator(numsim):
    numHead=0
    numTail=0
    for i in range(numsim):
        outcome=random.choice(HoT)
        print(outcome)
        if outcome=="Heads":
            numHead=numHead+1
        elif outcome=="Tails":
            numTail=numTail+1
    numHead=str(numHead)
    numTail=str(numTail)
    print("\n"+numHead+ " heads flipped and "+numTail+" tails flipped.")

#Main
coinFlipSimulator(500)
