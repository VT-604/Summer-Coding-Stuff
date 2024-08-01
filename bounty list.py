#VT-604
#7/25
#Bounty Hunter's List
#Initial
targets=[]
error=0
#Functions
#Main
name=input("Please enter your name: ")
print("Welcome to the Mercenary's Guild, "+name+".")
while True:
    print("\nWhat would you like to do today?: ")
    print("\n1. Add target \n2. View targets \n3. Report completion \n4. Edit target names \n5. Report completion for all \n6. Sort targets alphabetically \n7. Count number of targets \n8. Exit")
    option=input("Option: ")
    if option=="1":
        targetName=input("Please input the name of the target: ")
        if targetName==name:
            print("\nWhy did you put yourself on the list? That's not allowed.")
        else:
            targets.insert(0,targetName)
            print("\nTarget successfully posted. ")
    elif option=="2":
        print("\n")
        print(targets)
    elif option=="3":
        targetName=input("Please input the name of the deceased: ")
        targets.remove(targetName)
        print("\nTarget successfully removed. ")
    elif option=="4":
        targetName=input("Please input the name of the target you wish to edit: ")
        targets.remove(targetName)
        targetName=input("Please input the new name of the target: ")
        targets.insert(0,targetName)
        print("\nTarget successfully updated. ")
    elif option=="5":
        sure=input("\nAre you sure? Y/N")
        if sure=="Y":
            targets.clear()
            print("\nTargets successfully removed. ")
        elif sure=="N":
            print("\nok.")
        else:
            print("\nThat's not a valid option, so we're going to assume it's a 'N'")
    elif option=="6":
        targets.sort()
        print("\nTargets successfully sorted. ")
    elif option=="7":
        targetNum=str(len(targets))
        print("\n"+targetNum+" targets currently in list.")
    elif option=="8":
        sure=input("\nAre you sure? Y/N")
        if sure=="Y":
            print("\nSee you another day, "+name+".")
            break
        elif sure=="N":
            print("\nok.")
        else:
            print("\nThat's not a valid option, so we're going to assume it's a 'Y'")
    else:
        if error==0:
            print("\nIncorrect input. Please try again")
        elif error>=1:
            print("\nIncorrect Input. Again. (Hint: Please choose a number from 1 to 4)")
