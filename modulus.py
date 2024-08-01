#VT-604
#7/25
#Initial
import random
x=random.randint(0,255)
#Functions
def even_or_odd(num):
    if num%2==0:
        print("Even")
    elif num%2==1:
        print("Odd")
#Main
even_or_odd(x)
print(x)
