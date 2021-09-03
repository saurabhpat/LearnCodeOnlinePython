# Program to calculate shopping cart total_item_costs

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
