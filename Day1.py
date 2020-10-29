# Question :
# There was a teacher in a small town who loves coding and he wants to create a program which prints out
# the whole multiplication table of an entered number for his students. Can you help him write a program in python?


n = input("Enter the number of multiplicand : ")
y = int(input("Enter the number of multiplier :  "))
for i in range(1, y+1):
    print(f"{n} * {i} = {int(n) * int(i)}")
