#day8_practice - python SQL Functions with Finance dataset

# Exercise 1: Shop_Sales
# Query 1
import pandas as pd
import sqlite3

# define all you functions
def calculate_profit(Revenue, Cost):
    return Revenue - Cost

def Highest_profit(Revenue, Cost):
    profit = Revenue - Cost
    Highest_profit = max(profit)
    return {
        "Revenue": Revenue,
        "Cost": Cost,
        "Proft": profit,
        "Highest Profit": Highest_profit,
    }

# Create SQL connection and pandas
conn = sqlite3.connect(r"C:\Users\benkb\My_python_learning\Finance.db")

# Query the Month_Revenue_Cost data

print("==== Shop & Sales ====")
# Declare variables
show_all = "SELECT * FROM Shop_sales"
# Declare data frame df for All Query

df = pd.read_sql(show_all,conn)
print(df)
print()

# Declare variable for Profit
df["Profit"] = df.apply(lambda row: calculate_profit(row["Revenue"], row["Cost"]), axis=1)
print("==== Shop & Sales  Profit colunm ====")
print(df)
print()
print("==== Shop & Sales  Profit colunm ====")
df["Profit"] = df["Revenue"] - df["Cost"]
print(df)
print()


largerCost = "SELECT * FROM Shop_sales WHERE Cost > 3200" 
df1 = pd.read_sql(largerCost,conn)
print("==== Shop & Sales  Month WHERE costs are greater than 3200 ====")
print(df1)

df["Profit"] = df["Revenue"] - df["Cost"]
best_row = df.loc[df["Profit"].idxmax()]
print("Highest Profit", best_row["Profit"])
print("Month with the highest Profit:", best_row["Month"])
print()
top_months  = df[df["Profit"] == df["Profit"].max()]
print(top_months)
conn.close

print("=============================================================================================")

print("========== Exercise 2: Freelance_Income Table")
print()
QueryAllFreelance = "SELECT * FROM freelance_income"
df2 = pd.read_sql(QueryAllFreelance,conn)
print(df2)
print()

df2["profit"] = df2["Revenue"] - df2["Cost"]
print(df2)
print()
df2["Profit"] = df2.apply(lambda row: calculate_profit(row["Revenue"] , row["Cost"]), axis=1)
print(df2)                      
