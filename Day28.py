# Question :
# Dave is 13, 772, 160 minutes old in age, can you calculate his age in year

# Solution :
# min/60 -> 1 hr
# 24 hr -> 1 day
# 365 days -> 1 year

import math


def min_to_year(minutes):
    return ((minutes/60)/24)/365


print("Dave's age is ", math.floor(min_to_year(13772160)))
