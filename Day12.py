# Question :
# The number of red blood corpuscles in one
# the cubic milimeter is about 5,000,000 and the
# number of white blood corpuscles in one cubic
# the milimetre is about 8,000. What, then, is the ratio
# of white blood corpuscles to red blood corpuscles?
# Aspect Ratio should be as an int value?

# References :
# https://docs.python.org/3.8/library/fractions.html
# https://www.geeksforgeeks.org/fraction-module-python/

from fractions import Fraction

no_of_rbc = 5000000
no_of_wbc = 8000

# ratio = no_of_wbc / no_of_rbc

# print("Ratio : ",ratio," Type : ",type(ratio))
# print("Ratio of WBC to RBC : ", Fraction(ratio))
# print("Ratio of WBC to RBC : ", Fraction(no_of_wbc/no_of_rbc))
print("Ratio of WBC to RBC : ", Fraction(no_of_wbc, no_of_rbc))
