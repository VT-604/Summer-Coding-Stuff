#VT-604
#7/15
#Global vs Local Scope

#Initial
import turtle
import random
#Global Variables/Scope, can be used anywhere
x="Hello"
y="World"

#Functions
def myFunc():
    global x
    global y
    x="Goodbye"
    y="World!"
    print(x)
    print(y)
#Main
myFunc()
print(x)
print(y)
