# Question :
# The temperature recorded at 8AM is n deg Celsius.
# What is the equivalent of this temperature in degrees Fahrenheit?
# n is user entered value.

def celsius_to_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32


n = float(input("Enter the temperature recorded in Celsius : "))
print("Equivalent temperature in Fahrenheit : ", round(celsius_to_fahrenheit(n), 2))
