
print("================== Day 11: Mini Finance Project =================")

import pandas as pd

finance_project = [
    {"Month": 1, "Revenue": 3200, "Cost": 2900},
    {"Month": 2, "Revenue": 3300, "Cost": 2950},
    {"Month": 3, "Revenue": 3100, "Cost": 3050},
    {"Month": 4, "Revenue": 3400, "Cost": 3000},
    {"Month": 5, "Revenue": 3250, "Cost": 3100},
    {"Month": 6, "Revenue": 3350, "Cost": 3150},
    {"Month": 7, "Revenue": 3150, "Cost": 3200},
    {"Month": 8, "Revenue": 3450, "Cost": 3300},
    {"Month": 9, "Revenue": 3100, "Cost": 2950},
    {"Month": 10, "Revenue": 3600, "Cost": 3250},
    {"Month":11, "Revenue": 3400, "Cost": 3000},
]

df_fin = pd.DataFrame(finance_project)
df_fin["Profit"] = df_fin["Revenue"] - df_fin["Cost"]

print()
print(" ============ Task 1 Add profit Column ================ ")
print(df_fin)
print()
print(" ============ Task 2 Group by Month to show Total Revenue , Cost and Profit ================ ")
print()
groupby_fin =  df_fin.groupby("Month").sum()
print(groupby_fin)
group_agg = df_fin.groupby("Month").agg({
    "Revenue": "sum",
    "Cost": "sum",
    "Profit": "sum"
})
print()
print(group_agg)
print(" ============ Task 3 find the month with the highest total Profit ================ ")
print()
group_max = max(df_fin.groupby(["Month", "Profit"]))
print(group_max)
highest_profit = group_agg["Profit"].max()
best_Profit_Month = group_agg["Profit"].idxmax()
print("Highest profit:", highest_profit)
print("Highest profit Month:", best_Profit_Month)
# find all the months that have max profits
print()
best_months = df_fin[df_fin["Profit"]== highest_profit]
print(best_months)
