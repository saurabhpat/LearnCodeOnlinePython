# Question :
# Lucille spent 12% of her weekly earnings on
# DVDs and deposited the rest into her savings
# account. If she spent $42 on DVDs, how much
# did she deposit into her savings Account?

percent_spent_dvd = 0.12
percent_saved = 1 - percent_spent_dvd

amount_spent_dvd = 42

amount_saved = percent_saved * amount_spent_dvd / percent_spent_dvd

print("Amount deposited in Savings Account : ", amount_saved)
