
# ====== Day 12 Mini Project ================================
print(" ======= Day 12: Mini Finance Project ======== ")
data5 = [
    {"Month": "1", "Revenue": "3200", "Cost": "2900"},
    {"Month": "2", "Revenue": None, "Cost": "2950"},
    {"Month": "3", "Revenue": "3100", "Cost": "3050"},
    {"Month": "4", "Revenue": "3400", "Cost": None},
    {"Month": "4", "Revenue": "3400", "Cost": None},
    {"Month": "5", "Revenue": "3250", "Cost": "3100"},
]

df5 = pd.DataFrame(data5)

print("====== Before updated Clean version of Finance Table =======")
print(df5)

df5["Month"] = pd.to_numeric(df5["Month"])
df5["Revenue"] = pd.to_numeric(df5["Revenue"])
df5["Cost"] = pd.to_numeric(df5["Cost"])

df5 = df5.drop_duplicates()
df5["Revenue"] = round(df5["Revenue"].fillna(df5["Revenue"].mean()),1)
df5["Cost"] = round(df5["Cost"].fillna(df5["Cost"].mean()),1)

df5["Profit"] = df5["Revenue"] - df5["Cost"]

print()
print("====== Updated Clean version of Finance Table =======")
print(df5)