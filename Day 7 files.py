# Day 7 files

import csv

print("=== Day 7: CSV Files ===")

# Exercise 1: Read CSV
print("\n1. All rows:")
with open('monthly_finances.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)