#Day 9 file handling + CSV + pandas

print("==== Exercise 1: File Handling basic ====")



import pandas as pd

def calculate_profit(Revenue, Cost):
    return Revenue - Cost

df = pd.read_csv(r"C:\Users\benkb\My_python_learning\Sales_data.csv")
df["Profit"] = df.apply(lambda row: calculate_profit(row ["Revenue"], row["Cost"]), axis=1)

print(df.head())


df.to_csv(r"C:\Users\benkb\My_python_learning\sales_output.csv", index=False)

print("==========================================================")

print(df)
print("==========================================================")

print(df.tail())

print("==== Exercise 2: File Handling basic ====")
print()

def calculate_kept(Customers , Returns):
    return Customers - Returns

df2 = pd.read_csv(r"C:\Users\benkb\My_python_learning\monthly_customers.csv")

df2["Kept_Customers"] = df2.apply(lambda row: calculate_kept (row ["Customers"], row["Returns"]) , axis= 1)
best_row = df2.loc[df2["Kept_Customers"].idxmax()]
print(df2)
print()
print("Highest Month of Kept Customers:", best_row["Month"])
print()
top_months  = df2[df2["Kept_Customers"] == df2["Kept_Customers"].max()]
print()
print(top_months)

df2.to_csv(r"C:\Users\benkb\My_python_learning\monthly_customers_output.csv", index=False)
print("=========================================================================================")
print("==== Exercise 3: File Handling basic ====")

df3 = pd.read_csv(r"C:\Users\benkb\My_python_learning\finance_day9.csv")
print(df3)
print()
def calculate_profit(Revenue, Cost):
    return Revenue - Cost
def calculate_profit_rate(Revenue, Cost):
    profit = Revenue - Cost
    return round((profit / Revenue)*100, 2)

df3["Profit"] = df3.apply (lambda row: calculate_profit (row["Revenue"], row["Cost"]), axis=1)
df3["Profit_Rate"] = df3.apply (lambda row: calculate_profit_rate (row["Revenue"], row["Cost"]), axis=1)
print(df3)
print()
Highest_Profit  = df3[df3["Profit"] == df3["Profit"].max()]
Negative_Profit = df3[df3["Profit"] < 0]
print("==== Highest Profit ====")
print(Highest_Profit)
print("==== Negative Profit ====")
print(Negative_Profit)

df3.to_csv(r"C:\Users\benkb\My_python_learning\finance_day9_Output.csv",index=False)