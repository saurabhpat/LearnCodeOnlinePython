# Question :
# Can you help Alex to print double sided stair-case pattern in Python.
#     * *
#     * *
#   * * * *
#   * * * *
# * * * * * *
# * * * * * *
n = int(input("Enter the staircase count : "))
for i in range(1, n + 1):
    print("   " * (n - i), " * " * i * 2, "   " * (n - i))
    print("   " * (n - i), " * " * i * 2, "   " * (n - i))
