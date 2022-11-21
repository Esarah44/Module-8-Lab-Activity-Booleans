#List and functions
#Sara Hernandez
#November 18,2022
#The function returns True if there is 4 in the list, False otherwise

import random

num1 = random.randint(1,5)
num2 = random.randint(1,5)
num3 = random.randint(1,5)
num4 = random.randint(1,5)
num5 = random.randint(1,5)

numlist =[num1, num2, num3, num4, num5]

def findfour(numlist):
    if numlist[0]==4 or numlist[1]==4 or numlist[2]==4 or numlist[3]==4 or numlist[4]==4:
        return True
    else:
        return False

findfour_result = findfour(numlist)
print(findfour_result)

