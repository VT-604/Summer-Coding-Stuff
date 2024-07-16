#VT_604
#7/10
#Secret Number Game

#Initialize
import random
#Functions
def guess():
    x=False
    while x:
        secret=random.randint(1,10)#generates random numbers
        guess=int(input("Guess a number from 1 to 10: "))#input your guess
        if secret == guess:#if the secret number is the same as your guess
            print("Congratulations!!! You won a game with only a 10% chance of winning!")#win message ( also the percentage does not break the code)
            x=True
        else:#if secret number is NOT the same as your guess
            print("Aw dang it! You got it wrong... Here's the correct answer: ")#lose message
            print(secret)#reveals answer
#Main
guess()

