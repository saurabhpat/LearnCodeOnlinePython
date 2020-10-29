# Question :
# Write a Python program that accepts two integers from the user and then
# prints the sum, the difference , the product, the average, the maximum(the larger of two integers)
# the minimum(the smaller of two integers).

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))

print("Sum : ", num1+num2)
print("Difference : ", num1-num2)
print("Product : ", num1*num2)
print("Average : ", (num1 + num2) / 2)
print("Max : ", max(num1, num2))
print("Min : ", min(num1, num2))
