#Name
#Date
#Conditionals

#Initial
import random
#Functions

#Mueseum Ticket Prices
def museTicket(age):
    if age<18:
        print("Price: $10")
    elif age>=18 and age<60:
        print("Price: $20")
    else:
        print("Price:$15")
#Main
randage=random.randint(0,100)
print(randage)
museTicket(randage)
