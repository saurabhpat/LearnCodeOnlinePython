# Question :
# Write a python program to takes the user for a distance(in meters) and
# the time was taken(as three numbers: hours, minutes and seconds) and
# display the speed in miles per hour.

def metres_to_miles(distance):
    return distance / 1609


def time_in_hours(hour, minutes, seconds):
    return hour + (minutes/60) + ((seconds / 60)/60)


d_metres = float(input("Enter the distance in meters : "))

time = input("Enter the time in hours,minutes,seconds separated by colon : ").split(":")
h, m, s = int(time[0]), int(time[1]), int(time[2])

d = metres_to_miles(d_metres)
t = time_in_hours(h, m, s)

print("Speed in miles per hour : ", round((d/t), 4))
