# Question :
# If Julius has j books and Nancy has n, how many books do they have altogether?
# Convert and print as an Roman Number.
# j and n are user entered value.

# Reference :
# https://stackoverflow.com/questions/28777219/basic-program-to-convert-integer-to-roman-numerals

def num_to_roman(num):
    roman_num_map = [(1000, 'M'), (900, 'CM'), (500, 'd_metres'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                     (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    roman = ''

    while num > 0:
        for i, r in roman_num_map:
            while num >= i:
                roman += r
                num -= i
    return roman


j = int(input("Enter number of books Julius has : "))
n = int(input("Enter number of books Nancy has : "))

total_books = j + n

print("Total books Julius : ", num_to_roman(total_books))
