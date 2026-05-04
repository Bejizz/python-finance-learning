print("===== Practice ========")

import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\Users\benkb\My_python_learning\Finance.db")

#Revenue = 3000
#Expense = 1200

#Create SQL QUERY Variables
def profit_cal (Income, Expense):
    return Income - Expense 

def calc_profit (Income, Expense):
    profit = (Income - Expense)
    profit_rate = round((100 * profit / Income), 2)
    return {"profit": profit,
            "profit rate": profit_rate,
            "Income" : Income,
            "Expense" : Expense
            }

R = 3000
E = 1500

print(calc_profit(R, E))

query_alldata = ("SELECT * FROM monthly_finances")
df = pd.read_sql(query_alldata, conn)
print("==== Monthly Finance Data ====")
print(df)
print("===============================================")
query_profit = ("SELECT Month, Income, Expenses FROM monthly_finances")
df1 = pd.read_sql(query_profit,conn)
df1["profit"] = df1["Income"] - df1["Expenses"]
print(df1)

print("===============================================")
df2 = pd.read_sql("SELECT Month, Income, Expenses FROM monthly_finances",conn)
df2["profit"] = df2.apply(lambda row: profit_cal (row["Income"],row["Expenses"]), axis=1 )

print(df2)
print("=============================================================")

df3 = pd.read_sql("""SELECT 
                        SUM(Income) AS Total_Income,
                        sum(Expenses) as Total_Expenses,
                        sum(Income) - sum(Expenses) as Total_Profit,
                        max(Income) as MaxIncome,
                        max(Expenses) as MaxExpenses,
                        max(Income) - max(Expenses) as Max_Profit
                    FROM monthly_finances
                  """
,conn)
print("=== Totals and Max Income & Expenses ===")
print(df3)







conn.close