#Boolean function
#Sara Hernandez
#November 20,2022
#Function that uses a lis to return True if it is a leap year or False otherwise
import calendar

Leap_year = [1940, 1900, 1992, 1978, 2004, 2032, 2022, 2026, 2000, 2018, 1720]

def is_leap(leapyear):
    if (leapyear % 4 == 0):
        if (leapyear % 100 == 0):
            if (leapyear % 400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap

leap_years = []

for i in Leap_year:
    if is_leap(i) == True:
        leap_years.append(i)


leap_years2 = []

for j in Leap_year:
    if calendar.isleap(j) == True:
        leap_years2.append(j)

print("The results of my function are", leap_years, "which are the same from the calendar.isleap function", leap_years2)


