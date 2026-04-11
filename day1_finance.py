#Exercise1: Simple expense total

#Expenses

rent=850
transport=120
groceries=210
phone=35
coffee=45

TotalExpenses = (rent + transport+groceries+phone+coffee)
print("Total Expenses = ",TotalExpenses)
#=============================================
print("========================================================")

expense = {"Rent":850,
           "travel": 120,
           "food":210,
           "Mobile":35,
           "coffee":45
           }

total_expense = sum(expense.values())
print(f"Total expenses: £{total_expense}")
#============================================================
print("========================================================")
#Exercise 2 Income vs Expense
Income = 2500

Saving=(Income - total_expense)
print(f"Total Savings: £{Saving}")
#============================================================
print("========================================================")
#Exercise 3: Budget Check
Budgetlimit = 2000
if(total_expense < Budgetlimit):
    print("Under Budget")
print("========================================================")

print("Under Budget")
#Exercise 4: Multiple Months
Month1 = 1260
Month2 = 1345
Month3 = 1180

TotalMonths= {"Month1": 1260,
              "Month2": 1345,
              "Month3": 1180
              }
AverageMonth = sum(TotalMonths.values())/3
print(f"Average monthly spend: £{AverageMonth}")
print("========================================================")
#Calcuate the average
import statistics
print(statistics.mean([1260,1345,1180]))

print("========================================================")

#Exercise 5: Formatted Monthly report

print("===== Monthly Finance Report ====")
print(f"Total Income: £{Income}")
print(f"Total Expenses: £{total_expense}")
print(f"Total Savings: £{Saving}")
SavingRate = (1240 / 2500)*100
print(f"Savings Rate:{SavingRate}%")

print("==================================")
