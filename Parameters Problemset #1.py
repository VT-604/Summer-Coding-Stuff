#Name IVT
#Date 7/1
#Parameters Practice

#Initialization

#Functions
#1 Addition Function
#Create a function that takes a and b as paremeters
#and prints the sum of the two numbers
def addCalc(num1,num2):
    a=num1
    b=num2
    print(a+b)

#2 Greeting Function
#Create a function that takes a name as a parameter
#and prints a welcome message to that person
def greetFunc(fname,lname):
    a=fname
    b=lname
    print("Welcome to HECK, "+fname+" "+lname)

# Celsius to Fahrenheit Function
#Create a function thats takes celsius as a paremeter
#and prints the fahrenheit equivalent
def celsToFahr(celsius):
    C=celsius
    print((C*9/5)+32)
#Main
addCalc(1,2)
greetFunc("John","Smith")
celsToFahr(17)
