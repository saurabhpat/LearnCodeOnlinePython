# Question :
# ! A Chef was Cooking something special when required exact 200ml water but
# he does not have 200ml cup he has a 500ml cup and a 300ml cup but that dish
# required exactly 200ml water.
# Can you solve this problem in python

def required_water(big_cup, small_cup):
    return big_cup - small_cup


cup1 = 500
cup2 = 300

required_water = required_water(cup1, cup2)
print(required_water)
