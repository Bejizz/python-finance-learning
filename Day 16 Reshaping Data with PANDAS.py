print("=== Day 16 Reshaping Data with PANDAS ===")
print()
print("=== Part 1: Wide to Long with melt() ===")

import pandas as pd

df = pd.DataFrame({
    "Month": [1, 2, 3],
    "Revenue": [3200, 3300, 3100],
    "Cost": [2900, 2950, 3050]
})

df_long = df.melt(id_vars="Month", var_name="Metric", value_name="value")
print(df_long)
print()
print("=== Part 2: Long to wide with Pivot ===")

data = [
    {"Month": 1, "Metric": "Revenue", "Amount": 3200},
    {"Month": 1, "Metric": "Cost", "Amount": 2900},
    {"Month": 2, "Metric": "Revenue", "Amount": 3300},
    {"Month": 2, "Metric": "Cost", "Amount": 2950},
    {"Month": 3, "Metric": "Revenue", "Amount": 3100},
    {"Month": 3, "Metric": "Cost", "Amount": 3050},
]

df2 = pd.DataFrame(data)
df2_pivot = df2.pivot(index="Month", columns= "Metric", values="Amount")
print(df2_pivot)
print()
print("=== Part 3 Pivot Table and aggregation ===")

data1 = [
    {"Month": 1, "Category": "Food", "Amount": 500},
    {"Month": 1, "Category": "Transport", "Amount": 200},
    {"Month": 1, "Category": "Food", "Amount": 600},
    {"Month": 2, "Category": "Food", "Amount": 550},
    {"Month": 2, "Category": "Transport", "Amount": 250},
    {"Month": 2, "Category": "Food", "Amount": 700},
]

df3 = pd.DataFrame(data1)
df3_pivot = df3.pivot_table(index="Month", columns="Category",values="Amount", aggfunc=sum)
print(df3_pivot)
print()
print("=== Part 4 Add totals to pivot table ===")

df3_pivot["Total"] = df3_pivot.sum(axis= 1)
df3_pivot.loc["Total"] = df3_pivot.sum(axis=0)
print(df3_pivot)

print()
print("=== Part 5 Mini Reshaping Project ===")

data2 = [
    {"Month": 1, "Revenue": 3200, "Cost": 2900},
    {"Month": 2, "Revenue": 3300, "Cost": 2950},
    {"Month": 3, "Revenue": 3100, "Cost": 3050},
    {"Month": 4, "Revenue": 3400, "Cost": 3000},
]

df4 = pd.DataFrame(data2)
df4_wide = df4.melt(id_vars="Month", var_name="Metric", value_name="Amount")
print(df4_wide)
print()
df4_pivot = df4_wide.pivot_table(index="Month", columns="Metric", values="Amount")
df4_pivot["Profit"] = df4_pivot["Revenue"] - df4_pivot["Cost"]
print(df4_pivot)
