# Day 4 mini exercises - lists, adding, and removing items


expenses = [850, 120, 210, 35, 45]
print(expenses)

print(expenses[1])            #-------------- 120
print(expenses[-1])           #--------------- 45
print(expenses[-3])           #-------------- 210
print(expenses[0])            #-------------- 850

expenses.remove(120)   #-------------- 120
expenses.append(65)    #---------------- 65
print(expenses)

print(len(expenses))
print(sum(expenses))


print("==========================================================================")

Outgoings = {"rent": 850,
           "Travel" : 120,
           "Food": 210,
           "phone": 35,
           "coffee": 45
           }
print(f'Outgoings: £{Outgoings.values}')

Outgoings = {"rent": 850,
           "Travel" : 120,
           "Food": 210,
           "phone": 35,
           "coffee": 45}

TotalExpense = [850, 120, 210, 35, 45]
print(TotalExpense)

print("==========================================================================")

print("Rent:", TotalExpense[0])
print("Food:", TotalExpense[3])
print("Coffee:", TotalExpense[4])

print("==========================================================================")

TotalExpense.append(25)
TotalExpense.append(40)
TotalExpense.remove(45)
print("Updated - Total Expense list:", TotalExpense)
print("==========================================================================")

Total = sum(TotalExpense)
average = Total / len(TotalExpense)

print("==========================================================================")

print(f"Total Expense list: £{Total}")
print(f'Average expense: £{average:.2f}')
print(f'Highest Expense: £{max(TotalExpense)}')


print("==========================================================================")