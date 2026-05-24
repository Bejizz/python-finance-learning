#Day 13 Part 5: Mini SQL + pandas project

import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\benkb\My_python_learning\Finance.db")

data = {
    "Month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Revenue": [3200, 3300, 3100, 3400, 3250, 3350, 3150, 3450, 3100, 3600],
    "Cost": [2900, 2950, 3050, 3000, 3100, 3150, 3200, 3300, 2950, 3250]
}

df = pd.DataFrame(data)
#Send the data table to CSV and SQL
CSV_PATH = r"C:\Users\benkb\My_python_learning\Finance_Day13.csv"
df.to_csv(CSV_PATH , index=False)
df.to_sql("Finance_Day13" , conn, if_exists="replace", index=False)

print("=== Finance Data sent to CSV ===")
print()
print("=== Task1: SELECT ALL rows ===")
df1 = pd.read_sql("SELECT * FROM Finance_Day13",conn)
print(df1)
print("=== Task2: GROUP BY MONTH and TOTAL Revenue and Cost ===")
df2 = pd.read_sql("""SELECT Month, Sum(Revenue) as Total_Revenue, Sum(Cost) as Total_Cost
                  FROM Finance_Day13 GROUP BY Month;
                  """,conn)

df1["Profit"] = df1["Revenue"] - df1["Cost"]
print()
df1["Margin"] = round(df1["Profit"] / df1["Revenue"],2)

df2 = pd.read_sql("""SELECT Month, Revenue, Cost, (Revenue - Cost) as Profit
                FROM Finance_Day13 WHERE Profit < 0;
                  """,conn)

print()
print(df2)
print()
print(df1)
print()
Profit_less = df1[df1["Profit"] < 0] 
print("=== Loss Month of Profit ===")
print(Profit_less)
sorted_df1 = df1.sort_values("Profit", ascending=False)
top3 = sorted_df1.head(3)
print()
print(top3)