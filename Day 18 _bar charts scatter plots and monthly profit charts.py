print("==== Day 18 - bar charts scatter plots and monthly profit charts ====")

#Day 18 is about using charts to compare values and relationships. This is the storytelling layer that helps turn grouped numbers into something easier to explain.

#Concept explained simply
#You will practice: bar charts for comparisons, scatter plots for relationships,
#choosing the right chart for the right question.
print("==== Part 1: Bar Charts for Category totals ====")
print()
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Food", "Transport", "Bills", "Entertainment"],
    "Amount": [500, 150, 400, 250]
}
df = pd.DataFrame(data)
print(df)
plt.bar(df["Category"], df["Amount"])
plt.title("Spending by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()
print()
print("==== Part 2: Scatter Plots for Relationships ====")
print()
data1 = {
    "Cost": [100, 150, 200, 250, 300],
    "Profit": [20, 35, 50, 65, 80]
}
df1 = pd.DataFrame(data1)
print(df1)
plt.scatter(df1["Cost"], df1["Profit"])
plt.title("Cost vs Profit")
plt.xlabel("Cost")
plt.ylabel("Profit")
plt.show()
print()
print("==== Part 3: Building profit column and chart it ====")
print()
data2 = {
    "Month": [1, 2, 3, 4],
    "Revenue": [3000, 3200, 3100, 3500],
    "Cost": [2500, 2700, 2600, 2800]
}
df2 = pd.DataFrame(data2)
df2["profit"] = df2["Revenue"]- df2["Cost"]
print(df2)
plt.bar(df2["Month"], df2["profit"])
plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

plt.plot(df2["Month"], df2["Revenue"], marker='o', label="Revenue")
plt.plot(df2["Month"], df2["Cost"], marker='o', label="Cost")
plt.title("Monthly Revenue and Cost")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.show()

print("==== Part 4: Create a simple Business Summary ====")
# Create a simple monthly Business Summary with two Charts
print()
data3 = {
    "Month": [1, 2, 3, 4, 5],
    "Revenue": [3000, 3200, 3100, 3500, 3600],
    "Cost": [2500, 2700, 2600, 2800, 2900]
}
df3 = pd.DataFrame(data3)
df3["Profit"] = df3["Revenue"] - df3["Cost"]
print(df3)
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(df3["Profit"], marker='o')
plt.title("Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.subplot(1, 2, 2)
plt.bar(df3["Month"], df3["Revenue"])
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

