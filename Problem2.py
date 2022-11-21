#Function and max
#Sara Hernandez
#November 18,2022
#Function that takes three inputs from a user and prints the largest number without using max

def findingmax(a, b, c):
    if (a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    #elif (c >= a) and (c >= b):
    else:
        return c

n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
n3 = int(input("Enter the third number"))

print(findingmax(n1,n2, n3))