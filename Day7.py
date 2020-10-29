# Question :
# The city's bus system carries 1200000 people each day.
# How many people does the bus system carry each year?
# Solve without using *, / operator, bitwise or loop

# References :
# https://www.geeksforgeeks.org/product-2-numbers-using-recursion/

def total_capacity_yearly(n, d):
    if n < d:
        return total_capacity_yearly(d, n)
    elif d != 0:
        return n + total_capacity_yearly(n, d - 1)
    else:
        return 0


daily_capacity = 12000000
days = 365

year_capacity = total_capacity_yearly(daily_capacity, days)
print("Total people carried through bus system for a year :", year_capacity)
