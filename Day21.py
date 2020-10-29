# Question :
# Write a program that for a given hour and minutes values calculates an
# angle in degree between the hour and the minute hands. Check whether
# the minute hand overlapping the hour hand at a given time.

# References:
# https://www.geeksforgeeks.org/calculate-angle-hour-hand-minute-hand/

def angle_between_hr_and_minute(h, m):
    if m < 0 or h < 0 or m > 60 or h > 12:
        print("Not a valid hour and minute input.")
    if h == 12:
        h = 0
    if m == 60:
        m = 0
        h += 1
        if h > 12:
            h -= 12
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    angle = abs(hour_angle - minute_angle)

    angle = min(360 - angle, angle)

    if angle == 0:
        return print("Hour hand and Minute hand is overlapped.")
    else:
        return print("Angle between hour hand and minute hand is ", angle)


hour_hand = 0
minute_hand = 12

angle_between_hr_and_minute(hour_hand, minute_hand)
