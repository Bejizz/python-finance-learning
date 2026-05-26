print("==== Day 14: Merges and Joins Pandas and SQL ====")


import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\benkb\My_python_learning\Finance.db")

sales = ({
    "Month": [1, 2, 3, 4],
    "Revenue": [3200, 3300, 3100, 3400]
})

costs = ({
    "Month": [1, 2, 3, 4],
    "Cost": [2900, 2950, 3050, 3000]
})

df_Sales = pd.DataFrame(sales)
df_cost = pd.DataFrame(costs)

df = pd.merge(df_Sales, df_cost, on="Month", how= "inner")

df["Profit"] = df["Revenue"] - df["Cost"]

print(df)
#=========================================================================================

sales = ({
    "Month": [1, 2, 3, 4, 5],
    "Revenue": [3200, 3300, 3100, 3400, 3250]
})

costs = ({
    "Month": [1, 2, 3, 4],
    "Cost": [2900, 2950, 3050, 3000]
})

df1_sales = pd.DataFrame(sales)
df1_costs = pd.DataFrame(costs)

df_join = pd.merge(df1_sales, df1_costs, on= "Month", how="left")
print(df_join)
#=========================================================================================

df1_sales.to_sql("sales" , conn, if_exists= "replace", index=False)
df1_costs.to_sql("costs", conn, if_exists= "replace" , index=False)

print("=== Data tables created in SQL ===")

sc_data = ("""SELECT s.Month, s.Revenue, c.Cost, (s.Revenue - c.Cost) as Profit
             FROM sales s 
             LEFT JOIN costs c
             on s.Month = c.Month;
             """)
df2_join = pd.read_sql(sc_data, conn)
print()
print(df2_join)
print()
df2_join["Profit"] = df2_join["Revenue"]- df2_join["Cost"]
print(df2_join)
#==========================================================================================================
sales = pd.DataFrame({
    "Month": [1, 2, 3, 4],
    "Revenue": [3200, 3300, 3100, 3400]
})

categories = pd.DataFrame({
    "Month": [1, 2, 3, 4],
    "Category": ["A", "B", "A", "C"]
})

costs = pd.DataFrame({
    "Month": [1, 2, 3, 4],
    "Cost": [2900, 2950, 3050, 3000]
})

df3 = pd.merge(sales, categories,on= "Month" ,how= "inner")
df4 = pd.merge(df3, costs, on= "Month", how="inner")
df4["Profit"] = df4["Revenue"] - df4["Cost"]
print()
print(df4)

# ================== Part 5 Mini Project =========================================

sales = pd.DataFrame({
    "Month": [1, 2, 3, 4, 5, 6],
    "Revenue": [3200, 3300, 3100, 3400, 3250, 3350]
})

costs = pd.DataFrame({
    "Month": [1, 2, 3, 4, 5, 6],
    "Cost": [2900, 2950, 3050, 3000, 3100, 3150]
})

categories = pd.DataFrame({
    "Month": [1, 2, 3, 4, 5, 6],
    "Category": ["A", "B", "A", "C", "B", "A"]
})

df = pd.merge(sales, costs, on= "Month", how= "inner")
df1 = pd.merge(df,categories, on="Month", how="inner" )
df1["Profit"] = df1["Revenue"] - df1["Cost"]
print(df1)
print()
groupbyMonth = df1.groupby("Month").agg({
    "Category": "sum",
    "Revenue": "sum",
    "Cost": "sum",
    "Profit": "sum"
})
print(groupbyMonth)
print()
total_revenue = sum(df1["Revenue"])
total_cost = sum(df1["Cost"])
total_profit = sum(df1["Profit"])
group_agg = df1.groupby("Category").agg({
    "Revenue": "sum",
    "Cost": "sum",
    "Profit": "sum"
})
print("==== Group by Category Total Revenue, Cost and Profit ====")
print(group_agg)