# Question :
# SalesPerson Rita Drives 2052 miles in 6 days
# stopping at 2 towns each day. How many Kilometers
# does she average between stops?

# Solution :
# 2052 miles -> 6 days
# 2 towns stopped each days
# Day1 : A1->X1->B1

total_miles = 2052
total_kms = total_miles * 1.609344

avg_kms_per_day = total_kms / 6
# print("Average distance per day : ", avg_kms_per_day)

avg_kms_per_stops = avg_kms_per_day / 2
print("Average distance per stops : ", avg_kms_per_stops)
