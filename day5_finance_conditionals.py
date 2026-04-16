#========================== Day Python Conditionals

# Exercise 1: Budget Check 
income = 3200
expenses = 2900

if  income > expenses: 
    print("Saved money")
else:
    print("Over spent")

print("===================================================")

# Exercise 2: Savings Goal
Savings = 450
Goal = 500

if Savings >= Goal:
    print("Good Saving")
else:
    print("Keep Saving")

print("===================================================")
# Exercise 3: Transaction size

amount = 75
if amount < 50:
    print("Small")
elif amount > 200:
    print("Large")
else:
    print("Medium")

print("===================================================")

LeftoverIncome = (income - expenses)
savings_rate = LeftoverIncome / income * 100
print(f'Savings rate: {savings_rate:.2f}%')

if savings_rate >= 30:
    print("Excellent!")
elif savings_rate < 0:
    print("Emergency")
elif savings_rate >=15:
    print("Good!")
else:
    print("Tight!")


print("===================================================")