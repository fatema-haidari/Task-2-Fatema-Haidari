import csv
import sys
import os
total = 0
expenses = {}

while True:
    
        category = input("What did you spend on?:")
        amount = (int(input("How much? ")))

        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        
        if not os.path.exists("expenses.csv"):
            with open("expenses.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Category",0])

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            for category, amount in expenses.items():
                    writer.writerow([category, amount])

       
        choice = input("Add another expense? (y/n)")
        if choice.lower() == "n":
            break
with open("expenses.csv","r") as file:
            reader = csv.reader(file)
            for spent in reader:
                print(spent)
                amount = (float(spent[1]))
                total += amount
    

print("Total Expense",total)
            




