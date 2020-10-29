# Question :
# Mr Richard Tupper is purchasing gifts for his
# family. So far he has purchased the following:
# 1. 3 Sweaters, each valued at $68
# 2. One Computer game valued at $75
# 3. 2 bracelets each valued at $43
# Later, he returned one of the bracelets for a full
# refund and received a $10 rebate on the
# Computer game. What is the total cost for the gifts
# after the refund and rebate?
# Calculation part of the program should be under three lines.

total_amt_sweaters = 3 * 68
total_amt_computer_game = 1 * 75
total_amt_bracelets = 2 * 43
refund = 43
rebate = 10
total_amt = total_amt_computer_game + total_amt_bracelets + total_amt_sweaters
total_amt = total_amt - refund - rebate

print("Total Cost of Gifts : ", total_amt)
