# Question :
# Write a python program to input centimeter and convert to inch, meter and kilometer

length_cm = float(input("Enter the length in centimeter : "))

length_inch = length_cm / 2.54
length_m = length_cm / 100
length_km = length_cm / 100000

print("Length in inch : ", round(length_inch, 3))
print("Length in meters : ", round(length_m, 3))
print("Length in kilometers : ", round(length_km, 3))
