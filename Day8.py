# Question :
# On a Certain day, the nurses at a hospital worked the following number of hours:
# Nurse Howard worked 8 hours
# Nurse Pease worked 10 hours
# Nurse Campbell worked 9 hours
# Nurse Grace worked 8 hours
# Nurse McCarthy worked 7 hours
# and Nurse Murphy worked 12 hours.
# What is the average number of hours worked per nurse on this day?
# Average should be a float value

# nurse_hrs = [8,10,9,8,7,12]

nurse_hrs_dict = {"Howard": 8, "Pease": 10, "Campbell": 9, "Grace": 8, "McCarthy": 7, "Murphy": 12}

# print("Average working hours : ",sum(nurse_hrs)/len(nurse_hrs))

average_number_hrs = sum(nurse_hrs_dict.values()) / len((nurse_hrs_dict.values()))
print("Average working hours : ", average_number_hrs)
