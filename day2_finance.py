# Day 2 Finance Python Learning =======
# DAY 2 MINI 5 EXERCISES ====  Budget

income = 3200         #int
expenses = {"rent" : 950,
            "transport": 150,
            "food": 280
            }
savings = (income - sum(expenses.values()))
print(f"Savings: £{savings}")

tax_rate = 0.20       #float
is_profitable = True  #bool

print(type(income))
print(type(savings))
print(type(tax_rate))
print(type(is_profitable))

print("============================================================")

Rent = 950
Transport = 150
Groceries = 280

print("============================================================")

print("==== April Budget====")
print(f"Income:    £{income}")
print(f"Rent:      £{Rent}")
print(f"Transport: £{Transport}")
print(f"Groceries: £{Groceries}")
print(f"Savings:   £{savings}")
print("==================== ")

print("============================================================")

Saving_Rate = savings / income * 100
print(f"Savings Rate: {Saving_Rate}%")
