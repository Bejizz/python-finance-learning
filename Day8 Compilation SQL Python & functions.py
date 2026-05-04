#Day8 Compilation SQL Python & functions

import sqlite3
import pandas as pd


def add_two(a, b):
    return a + b


def calculate_profit(revenue, cost):
    return revenue - cost


def calculate_profit_summary(revenue, cost):
    profit = revenue - cost
    profit_rate = round((profit / revenue) * 100, 2) if revenue != 0 else 0
    return {
        "revenue": revenue,
        "cost": cost,
        "profit": profit,
        "profit_rate": profit_rate,
    }


conn = sqlite3.connect(r"C:\Users\benkb\My_python_learning\Finance.db")

print("=== DAY 8: Python + SQL + Functions ===")
print("Check add_two function:", add_two(10, 5))
print()

query_all = "SELECT * FROM monthly_finances ORDER BY Month"
df = pd.read_sql(query_all, conn)
print("=== Full monthly_finances table ===")
print(df)
print()

df["Profit"] = df.apply(lambda row: calculate_profit(row["Income"], row["Expenses"]), axis=1)
df["Profit_Rate"] = (df["Profit"] / df["Income"] * 100).round(2)

print("=== With calculated Profit and Profit_Rate ===")
print(df)
print()

query_expenses = """
SELECT *
FROM monthly_finances
WHERE Expenses > 3000
ORDER BY Month
"""
df1 = pd.read_sql(query_expenses, conn)
print("=== Query 1: Months where Expenses > 3000 ===")
print(df1)
print()

query_totals = """
SELECT
    SUM(Income) AS total_income,
    SUM(Expenses) AS total_expenses,
    ROUND(AVG(Savings_Rate), 2) AS avg_savings_rate
FROM monthly_finances
"""
df2 = pd.read_sql(query_totals, conn)
print("=== Query 2: Totals and average savings rate ===")
print(df2)
print()

query_negative = """
SELECT
    Month,
    Income,
    Expenses,
    Savings_Rate,
    (Income - Expenses) AS net_savings
FROM monthly_finances
WHERE Savings_Rate < 0
"""
df3 = pd.read_sql(query_negative, conn)
print("=== Query 3: Overspending months ===")
print(df3)
print()

print("=== Profit summaries per month ===")
for _, row in df.iterrows():
    summary = calculate_profit_summary(row["Income"], row["Expenses"])
    print(f"Month {int(row['Month'])}: {summary}")
print()

summary_df = df[["Month", "Income", "Expenses", "Profit", "Profit_Rate", "Savings_Rate"]]
print("=== Final summary table ===")
print(summary_df)

conn.close()