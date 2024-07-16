#VT-604
#7/16
#Clickbait Headline Generator

#Initialize
import random
#Functions
def headlineGenerator():
    print("Welcome to the Clickbait Headline Generator. Would you like to generate one? Y/N")
    option=input("Option: ")
    if option=="Y":
        economy=True
        while economy==True:
            type=random.randint(1,5)
            print("You chose Yes.")
            print("Great! Now let's create one!\n")
            if type==1:
                print(basicHeadline())
                print("Would you like to try again? Y/N")
                again=input("Option: ")
                if again=="Y":
                    economy=True
                elif again=="N":
                    print("Wow who would've thought. You're a slightly morally upright person.")
                    economy=False
            elif type==2:
                print(companyHeadline())
                print("Would you like to try again? Y/N")
                again=input("Option: ")
                if again=="Y":
                    economy=True
                elif again=="N":
                    print("Wow who would've thought. You're a slightly morally upright person.")
                    economy=False
            elif type==3:
                print(foundHeadline())
                print("Would you like to try again? Y/N")
                again=input("Option: ")
                if again=="Y":
                    economy=True
                elif again=="N":
                    print("Wow who would've thought. You're a slightly morally upright person.")
                    economy=False
            elif type==4:
                print(giftHeadline())
                print("Would you like to try again? Y/N")
                again=input("Option: ")
                if again=="Y":
                    economy=True
                elif again=="N":
                    print("Wow who would've thought. You're a slightly morally upright person.")
            elif type==5:
                print(interestHeadline())
                print("Would you like to try again? Y/N")
                again=input("Option: ")
                if again=="Y":
                    economy=True
                elif again=="N":
                    print("Wow who would've thought. You're a slightly morally upright person.")
            else:
                print("error")
    elif option=="N":
        print("Wow who would've thought. You're actually a morally upright person.")
    else:
        print("error")
def basicHeadline():
    object=input("Enter an object:")
    type=input("Enter a type of person (plural please): ")
    return("Are "+type+" Killing the "+object+" Industry?\n")

def companyHeadline():
    pronoun=input("Enter an object pronoun: ")
    place=input("Enter a place: ")
    noun=input("Enter a noun: ")
    object=input("Enter an object: ")
    return("Big Corpos Hate "+pronoun+"! "+"See How This "+noun+" From "+place+" Invented a Cheaper And Better "+object+"!\n")

def foundHeadline():
    pronoun=input("Enter a possesive pronoun: ")
    noun=input("Enter a noun: ")
    place=input("Enter a personal space: ")
    return("You Won't Believe What This "+noun+" Found In "+pronoun+" "+place+"\n")

def giftHeadline():
    number=input("Enter a number: ")
    noun=input("Enter a noun: ")
    place=input("Enter a place: ")
    return("Top "+number+" Things To Give To Your "+noun+" From "+place+"\n")

def interestHeadline():
    number=input("Enter a number: ")
    nouns=input("Enter a plural noun: ")
    number2=input("Enter a second number that's less than the first: ")
    return("Top "+number+" Reasons Why "+nouns+" Are More Interesting Than You Think. (Number "+number2+" Will Suprise You!)\n")

#Main
headlineGenerator()
