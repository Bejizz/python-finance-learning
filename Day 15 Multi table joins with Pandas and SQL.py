print("=== Day 15 Multi table joins with Pandas and SQL ===")
print()
print("=== Part 1: Merge Two Table ===")
import pandas as pd

sales = pd.DataFrame({
    "Month": [1, 2, 3, 4, 5],
    "Revenue": [3200, 3300, 3100, 3400, 3250]
})

costs = pd.DataFrame({
    "Month": [1, 2, 3, 4, 5],
    "Cost": [2900, 2950, 3050, 3000, 3100]
})

df_join = pd.merge(sales , costs, on= "Month", how= "inner")