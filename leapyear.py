#VT-604
#7/25
#Initial
#Functions
def leapYear(year):
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
#Main
print(leapYear(2500))
print(leapYear(2000))
print(leapYear(2022))
print(leapYear(2024))
