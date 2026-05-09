#day 8 functions
#========================== Exercise ===========================
def add_two (a,b):
    result = a + b
    return result

x = 6
y = 5

total = add_two(x,y)

print(f'Total={total}')

# ========================== Finance Task ========================

def calc (x,y):
    profit = x - y
    return profit

Revenue = 50
Cost = 25

Net_Profit = calc(Revenue,Cost)
print(f'Net Profit {Net_Profit}')

print("===============================================")

def Total_Profit(rev, cst):
    profit = rev - cst 
    return profit
income = 2000
expense = 2600

net_income = Total_Profit(income,expense)
print("Net Income",net_income)   

