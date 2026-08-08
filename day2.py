print("Welcome to the tip calculator!")
bill=float(input("what was the total bill? $"))
tip=int(input("How much tip would you like to give 10, 12, or 15 "))
people=int(input("How many people are going to split the bill "))
each_p=(bill+ (bill*(tip/100)))/people
each_p=round(each_p,2)
print(f"each person should pay: ${each_p}")