#Day 17: Date time and First Trend Chart

print("==== Part 1: Convert Date from String to Numeric ====")
import pandas as pd

data = {
    "Date": ["2026-01-05", "2026-01-12", "2026-02-03", "2026-02-20", "2026-03-01"],
    "Revenue": [200, 250, 300, 280, 320]
}

df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print()
df["Date"] = pd.to_datetime(df["Date"])
print()
print(df)
print(df.dtypes)

print("==== Part 2: Extract year, Month, and Weekday ====")

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
#df["Date"] = df["Date"].dt.weekday
df["DayName"] = df["Date"].dt.day_name()
df = df.sort_values("Date")
print()
print(df)
print("==== Part 3: Group Revenue by Month ====")
print()

monthly_revenue = df.groupby("Month")["Revenue"].sum().reset_index()
print(monthly_revenue)
print()
print("==== Part 4: Create Simple Line Chart of Monthly Revenue ====")
print()

import matplotlib.pyplot as plt

plt.plot(monthly_revenue["Month"], monthly_revenue["Revenue"], marker='o')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

print()
print("==== Part 5: Create a New DataFrame with Date and Revenue ====")
data1 = {
    "Date": ["2026-01-05", "2026-01-12", "2026-02-03", "2026-02-20", "2026-03-01", "2026-03-15"],
    "Revenue": [200, 250, 300, 280, 320, 180]
}
df1 = pd.DataFrame(data)
df1["Date"] = pd.to_datetime(df1["Date"])
print(df1)
df1["Year"] = df1["Date"].dt.year
df1["Month"] = df1["Date"].dt.month
df1["DayName"] = df1["Date"].dt.day_name()
print(df1)
print()
monthly_summary = df1.groupby("Month")["Revenue"].sum().reset_index()
print(monthly_summary)
print()
plt.plot(monthly_summary["Month"], monthly_summary["Revenue"], marker='o')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
