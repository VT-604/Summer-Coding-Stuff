#VT-604
#7/29
#Magic 8 Ball

#Initial
responses=["It is certain. ","Reply hazy, try again. ","Don’t count on it. ","It is decidedly so. ","Ask again later. ","My reply is no. ","Without a doubt. ","Better not tell you now. ","My sources say no. ","Yes definitely. ","Cannot predict now. ","Outlook not so good. ","You may rely on it. ","Concentrate and ask again. ","Very doubtful. ","As I see it, yes. ","Most likely. ","Outlook good. ","Yes. ","Signs point to yes. "]
import random
#Functions
def magic8():
    print("Welcome to Vitruvius's Virtual Magic 8 Ball. \nWhat would you like to ask today? \n(Note: Can only answer Yes or No questions.) \n")
    firstTime=0
    while True:
        if firstTime==0: #Checks if asking for the first time.
            question=input("Question: ")
            x=question.endswith("?") #Checks if the input ends with a "?"
            if x==True:
                print(question+"\n")
                print(random.choice(responses))
                again=input("Would you like to ask again? Y/N")
                if again=="Y":#There is a 5.26% chance to get the same response.
                    firstTime=firstTime+1
                elif again=="N":
                    print("\nWell then, goodbye!")
                    break
                else:
                    print("\nThat's not a valid answer, so we'll treat it as a yes. \n")
            else:
                print("Please ask a question. \n")
        elif firstTime>=1: #All of this stuff below is just for a different start when asking another question
            print("\nWell then, ask away.\n")
            question=input("Question: ")
            x=question.endswith("?")
            if x==True:
                print(question+"\n")
                print(random.choice(responses))
                again=input("Would you like to ask again? Y/N")
                if again=="Y":
                    firstTime=firstTime+1
                elif again=="N":
                    print("\nWell then, goodbye!")
                    break
                else:
                    print("\nThat's not a valid answer, so we'll treat it as a yes. \n")
            else:
                print("Please ask a question. \n")

#Main
magic8()
