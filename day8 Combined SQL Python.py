#day8 Combined SQL Python

import pandas as pd
import sqlite3
conn = sqlite3.connect(r"C:\Users\benkb\My_python_learning\Finance.db")
df1 = pd.read_sql("SELECT * FROM monthly_finances",conn)
print(df1)

print("=====================================================")


df2 = pd.read_sql(""" 
SELECT 
    Month,
    SUM(Income) as Total_Income,
    SUM(Expenses) as Total_Expenses,
    Round(avg(Savings_Rate),2) as Avg_Savings
FROM Monthly_Finances;
""", conn)
print("=== Query 2: Total Income, Expenses, and Average Savings Rate ====")
print(df2)

print("=======================================")

df3 = pd.read_sql("""
SELECT * FROM Monthly_Finances
WHERE Expenses > 3150
ORDER BY Month
""", conn)
print("==== Query 3 Expenses greater than 3150 ====")
print(df3)

# Query from Exercise Month, Income, Expenses, Saved income, and Savings_Pct
df4 = pd.read_sql("""
SELECT
    Month,
    Income,
    Expenses,
    Income - Expenses as Saved_Income_£,
    round(100*(Income - Expenses)/Income,3) as Savings_Pct
FROM Monthly_Finances
ORDER BY Month
""", conn)

print("==== Query 4: Monthly Balance ====")
print(df4)