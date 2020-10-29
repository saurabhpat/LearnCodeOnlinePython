# Question :
# There are 10 students in a class some students name are same to other students.
# Print the names that occur more than one time. All names should be in a single string
# Eg. str = 'Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar'

# References :
# https://www.geeksforgeeks.org/python-list-function-count/

student_names_str = input("Enter the name of 10 students separated with space: ")

student_names = student_names_str.split(" ")
print("Student name occur more than once are as follows: ",
      [[i, student_names.count(i)] for i in set(student_names) if student_names.count(i) > 1])
