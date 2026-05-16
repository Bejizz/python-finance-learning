
# Day 10 Mini Finance project (Lists, Dictionaries, loops and functions)

print("===== Mini Project Finance Project ======================")
finance_data = [
    {"Month": 1, "Revenue": 3200, "Cost": 2900},
    {"Month": 2, "Revenue": 3300, "Cost": 2950},
    {"Month": 3, "Revenue": 3100, "Cost": 3050},
    {"Month": 4, "Revenue": 3400, "Cost": 3000},
    {"Month": 5, "Revenue": 3250, "Cost": 3100},
    {"Month": 6, "Revenue": 3350, "Cost": 3150},
    {"Month": 7, "Revenue": 3150, "Cost": 3200},
    {"Month": 8, "Revenue": 3450, "Cost": 3300},
    {"Month": 9, "Revenue": 3100, "Cost": 2950},
    {"Month": 10, "Revenue": 3600, "Cost": 3250}
]
def calculate_profit(Revenue, Cost):
    Profit = Revenue - Cost
    return Profit

def calculate_profit_rate(Revenue, Cost):
    profit_rate = round((Revenue - Cost) / Revenue, 2)*100
    return profit_rate

print("===================== Updated Finance Table ======================")
for f_rows in finance_data:
    f_rows["Profit"] = calculate_profit(f_rows["Revenue"], f_rows["Cost"])
    f_rows["Profit_Rate"] = calculate_profit_rate(f_rows["Revenue"], f_rows["Cost"])
    print(f_rows)

best_profit = max(f_rows["Profit"] for f_rows in finance_data)
best_month = [f_rows for f_rows in finance_data if f_rows["Profit"] == best_profit]
total_finance_Profit = 0
total_months = 0
negative_fin_Profits = 0

for f_rows in finance_data:
    total_finance_Profit += f_rows["Profit"]
    total_months += 1
    if f_rows["Profit"] < 0:
        negative_fin_Profits += 1



print()
print("Total Finance Profit:", total_finance_Profit)
print()
print("Number of months", total_months)
print(len(finance_data)) # --------------------- Alternative method for calculating Average profit.
print()
print("=========== Average Profit ==========")
print("Average Profit", total_finance_Profit / total_months)
print()
print("Negative Profit", negative_fin_Profits)
print()
print("Highest Profit:" , best_profit)
print("Hightes profit month:", best_month)
