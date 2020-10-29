# Question :
# Write a python program to find if a given year is a leap year or not

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return print("Leap Year")
            else:
                return print("Not a Leap Year")
        else:
            return print("Leap Year")
    else:
        return print("Not a Leap Year")


input_year = int(input("Please enter the year : "))
leap_year(input_year)
