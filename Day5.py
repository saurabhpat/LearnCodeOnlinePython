# Question :
# During the last week track of training,
# Shoshanna achieves the following times in sec
# rounds - 66, 57, 54, 53, 64, 52, 59
# Found her best score using bubble sort

# References :
# https://www.geeksforgeeks.org/python-difference-between-sorted-and-sort/
# https://www.geeksforgeeks.org/bubble-sort/


def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


list_seconds = [66, 57, 54, 53, 64, 52, 59]
bubble_sort(list_seconds)
print(sorted(list_seconds))
print("Best Score : ", list_seconds[0])
