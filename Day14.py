# Question :
# How many ways can four students Ram, Anuj, Deepak and Ravi line up in
# a line, if the order matters?
# Print all the possible Combination.

# References :
# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
# https://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list
# https://www.geeksforgeeks.org/factorial-in-python/

import itertools

students = ["Ram", "Anuj", "Deepak", "Ravi"]
print(list(itertools.permutations(students)))
