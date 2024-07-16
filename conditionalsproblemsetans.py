#Name IVT
#Date 7/2
#Conditionals

#Initialization

#Functions

#1. Write a function with an age parameter that checks
#to see if a person is eligible to vote (>=18)
def voteAge(age):
    if age >=18:
        print("You can vote!")
    else:
        print("Sorry, but you can't vote...")
#2. Write a function with 3 integer parameters (a,b,c) that
#prints the largest of the three numbers
def bigNumber(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print (b)
    else:
        print(c)

#3. Write a function with a score parameter that prints the
#equivalent letter grade of that score (90+ = A, 80+ = B, etc)
def testGrade(score):
    if score>=90:
        print("You got an A!!")
    elif score>=80 and score<90:
        print ("You got a B!")
    elif score>=70 and score<80:
        print ("You got a C!?")
    elif score>=60 and score<70:
        print ("You got a D.")
    else:
        print ("You got an F...")
#Main
voteAge(int(input("Please enter your age: ")))
bigNumber(int(input("Please enter number a: ")),int(input("Please enter number b: ")),int(input("Please enter number c: ")))
testGrade(int(input("Please enter your score: ")))
