#day8_sqlite_connect

import os
print(os.getcwd())

##########################################

import sqlite3

conn = sqlite3.connect(r"C:\Users\benkb\My_python_learning\Finance.db")
#conn = sqlite3.connect("Finance.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM monthly_finances")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(cursor.fetchall())
