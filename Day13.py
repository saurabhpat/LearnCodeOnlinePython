# Question :
# 5th Graders kara and Rani both have lemonade
# stands. Kara sells her lemonade at 5 cents a glass
# and Rani sells hers at 7 cents a glass. Kara sold K number
# of glasses of lemonade today and Rani sold r number of glasses.
# Who made the most money and by what amount?
# k and r are user entered value..

k = int(input("Enter number of glasses Kara sold : "))
r = int(input("Enter number of glasses Rani sold : "))

total_sell_Kara = k * 5
total_sell_Rani = r * 7

if total_sell_Kara > total_sell_Rani:
    print("Kara sold more lemonade glasses than Rani by ", total_sell_Kara - total_sell_Rani)
elif total_sell_Rani > total_sell_Kara:
    print("Rani sold more lemonade glasses than Kara by ", total_sell_Rani - total_sell_Kara)
else:
    print("Kara and Rani sold equal number of lemonade glasses")
