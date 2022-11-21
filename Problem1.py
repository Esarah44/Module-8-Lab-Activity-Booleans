#Using Boolean value
#Sara Hernandez
#November 17,2022
#Function that returns True if two numbers are equal and False otherwise

import random

def equalitytest(num1, num2):
    return num1==num2

num_equality = False
counter = 0
while num_equality==False:
    counter += 1
    num1=random.randint(1,20)
    num2=random.randint(1,20)
    num_equality=equalitytest(num1,num2)
    if num_equality==True:
        print("It took", counter,"tries but the matching numbers are", num1, "and", num2)
