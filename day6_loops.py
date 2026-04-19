# Day6_loops
#pracrice examples
expenses = [850, 120, 210, 45, 60]
for amount in expenses:
    if amount > 210:
        print(f"Highest amount in the list is: {amount}")
    print(amount)
print("==================================================================")

for month in range(1,13):
    print(f"month: {month}")

print("==================================================================")

#Day 6 mini exercise sheet ================================================================

# Exercise 1: Print each expense

totalExpenses = [850,120,210,45,60]

for ind_amount in totalExpenses:
    print (ind_amount)
print("==================================================================")

# Exercise 2: Sum with a loop
listtotal = 0 # initialise the sum variable
for ind_amount in (totalExpenses):
    listtotal += ind_amount
print(listtotal)

print("==================================================================")
# Exercise 3: Count large expenses

for large in totalExpenses:
    if large > 200:
        print(large)
print("==================================================================")
# Exercise 4: Monthly Savings
income  = [3200, 3300, 3100, 3400, 3250, 3350]
expense = [2900, 2950, 3050, 3000, 3100, 3150]

for i in range(len(income)):
    if income[i] - expense[i] > 300:
        print(f'Month {i+1}: £{income[i]} and £{expense[i]}')
        print(f'Month {i+1}: Savings: £{income[i]-expense[i]}')
        print("============================================")
print("==================================================================")

x = len(income)
print(x)

Savinglist = [] # empty list store
for i in range(len(income)):
    Savings = income[i] - expense[i]
    Savinglist.append(Savings)
    
print("Savings", Savinglist)

# Exercise 5: Flag overspendprint("==================================================================")