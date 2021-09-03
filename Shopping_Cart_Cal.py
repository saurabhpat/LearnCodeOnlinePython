"""
write a Python program to implement a shopping cart price calculator. Our store sells four items and each item costs $1. Currently our store is offering some promotions. These are the promotions applied to each of the four items:

Item A = Full price only
Item B = Buy one get one free
Item C = 50% off
Item D = Full price only

Write a function or program that will calculate the total for a shopping cart based on the given prices and the given promotions. For example:

If the shopping cart contained “A, B, C, D” then the total would be $1 + $1 + $0.50 + $1 = $3.50 because Item C is 50% and even though Item B is buy one get one free there was only one item in the cart.

If the shopping cart contained “A, B, B, D” then the total would be $1 + $1 + $1 - $1 + $1 = $3 because Item B appeared in the cart twice so the second one was free.
"""

# Solution Starts 

# Number of following items bought 
no_of_item_A = int(input("Enter the numbers of items A bought: "))
no_of_item_B = int(input("Enter the numbers of items B bought: "))
no_of_item_C = int(input("Enter the numbers of items C bought: "))
no_of_item_D = int(input("Enter the numbers of items D bought: "))

# Applying Promotion Offers to Items

# Item A - Full Price only
total_cost_item_A = no_of_item_A

# Item B - Buy One Get One
""" 
Since 2 items of B will be bought at same price,
we needed to club those items as one and add the remaining items to get total costs
"""
total_cost_item_B = (no_of_item_B // 2) + (no_of_item_B%2) 

# Item C - 50% off
total_cost_item_C = no_of_item_C * 0.5

# Item D - Full Price only
total_cost_item_D = no_of_item_D

# Calculating total costs
total_item_costs = total_cost_item_A + total_cost_item_B + total_cost_item_C + total_cost_item_D

print("Total For Amount for a shopping Cart: ", total_item_costs)

#Solution Ends
