# Day3 Mini Exercise: Formatting + f-strings and decimals
price = 1234.5678
print(f"Price: {price:.2f}")

print("============================================================")
import decimal
income = 3200
savings = 1820
rate = savings / income * 100
print(f'Savings Rate: {rate:.2f}%')

print("============================================================")

big_total = 1234567.89784
print(f"£{big_total:,.2f}")
print("============================================================")
#using f'string method
res = f"{100000000:,}"
print(res)

num = 123456.1234567
#using string.format() method
resf= '{:,.2f}'.format(num)
print(resf)
print("============================================================")

#Full Budget with Formatting
# Declare Variables 
Income = 3200.50
Rent = 950.25
Transport = 150.75
Food = 280.30
Total_Expenses = {
                  "Rent":950.25,
                  "Transport": 150.75,
                  "Food": 280.30
                  }

Saved_Amt = Income - sum(Total_Expenses.values())
SavingsRate = (Saved_Amt / Income)*100

# Budgetting Table Formatted
print("==== April Budget ===========")
print(f'Income:       £{Income:,.2f}')
print(f'Rent:         £{Rent:,.2f}')
print(f'Transport:    £{Transport:,.2f}')
print(f'Groceries:    £{Food:,.2f}')
print(f'Savings:      £{Saved_Amt:,.2f}')
print(f"Savings %     {SavingsRate:.2f}%")
print("==============================")

print("========================================================")


a = 0.1
b = 0.2
total = a + b

print(total)                    #=================== unformatted number
print(f'Total: {total:.2f}')    #==================== formatted number




