# Question :
# Write a program to get the sum of n numbers
# Eg: Sum of 123 is 6
# n is user entered value

# Reference :
# https://www.programiz.com/python-programming/examples/natural-number-recursion

def sum_of_n(n):
    if n == 1:
        return n
    else:
        return n + sum_of_n(n - 1)


num = int(input("Enter the total number of digits : "))
print("Sum : ", sum_of_n(num))
