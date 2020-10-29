# Question :
# Find the square of a number without using multiplication and division operation

def square(n, total=0):
    for i in range(0, n):
        total += n

    return total


total_sum = 0
print("Square : ", square(5, total_sum))
