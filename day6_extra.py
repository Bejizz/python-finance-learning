# Day 6 Extra practice Exercises

# Exercise 1: Flag high expenses

expenses = [850, 120, 210, 45, 60, 950, 180]

for i in expenses:
    if i > 500:
        print(i,' HIGH')
    else:
        print(i, ' OK')
print("===================================")

# Exercise 2: Running total by month

monthly_income = [3200, 3300, 3100, 3400, 3250, 3350]
income = 0
for x in range(len(monthly_income)):
    income += monthly_income[x]
    print(f'month {x + 1}: cumulative £{monthly_income[x]} (£{income}) ')
print("=======================================")

# Exercise 3: Count expense by Category
transactions = [850, 120, 210, 950, 45, 180, 60, 3200]
small , medium, Large = 0 , 0, 0
for translen in transactions:
    if translen < 100:
        small+= 1
    elif translen > 499:
        Large+= 1
    else:
        medium+= 1
print(f'Small Transaction {small}')
print(f'Large Transaction {Large}')
print(f'Medium Transaction {medium}') 
print("=======================================")
    
# Exercise 4: Find best/worst month
Saving = [300, 350, 50, 400, 150, 200]
best = max(Saving)
worst = min(Saving)

print(f'Best Savings £{best}')
print(f'Worst Savings £{worst}')

print("=========================================")

# Exercise 5: Budget alert system
monthly_budget = [2600, 2950, 3100, 2450, 2850, 2700]
budget_limit = 2800
alert = 0
for b in range(len(monthly_budget)):
    alert =+ monthly_budget[b]
    if alert > budget_limit:
        print(f'Month {b+1}: Budget OVER {monthly_budget[b]}')
    elif alert < budget_limit:
        print(f'Month {b+1}: Budget UNDER {monthly_budget[b]}')
print("======================================================")