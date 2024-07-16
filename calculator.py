#Calculator
#Name
#7/10
#Initial
#Functions
def calculate():
    print("Welcome to Logoge's brand new calculator app.")
    while True:
        print("Please press one of the numbers from 1 to 5")
        print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Quit")
        option=input("Option: ")
        if option=="1":
            number1=float(input("What is your first number?: "))
            number2=float(input("What is your second number?: "))
            print(addition(number1,number2))
        elif option=="2":
            number1=float(input("What is your first number?: "))
            number2=float(input("What is your second number?: "))
            print(subtraction(number1,number2))
        elif option=="3":
            number1=float(input("What is your first number?: "))
            number2=float(input("What is your second number?: "))
            print(multiplication(number1,number2))
        elif option=="4":
            number1=float(input("What is your first number?: "))
            number2=float(input("What is your second number?: "))
            print(division(number1,number2))
        elif option=="5":
            print(quit())
            break
        else:
            print("Invalid command")
def addition(num1,num2):
    return(num1+num2)
def subtraction(num1,num2):
    return(num1-num2)
def multiplication(num1,num2):
    return(num1*num2)
def division(num1,num2):
    return(num1/num2)
def quit():
    return("Goodbye, USER")
#Main
calculate()
