import json
import os
from datetime import datetime 

def display_menu():
    print("-"*40)
    print("      Personal Expenses Tracker")
    print("-"*40)
    print("1. Add expenses")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. Filter by category")
    print("5. Delete expenses")
    print("6. Monthly summary")
    print("7. Exit")
    print("-"*40)
    
def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json") as file:
            return json.load(file)
    return []
    
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)
        
def get_date():
    today = datetime.today().strftime("%Y-%m-%d")
    
    date = input("Please input the date in YYYY-MM-DD format (Press enter for today): ")
    if date == "":
        return today
    
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError:
        print("Invalid date formatting, using todays date instead...")
        return today

def main():
    expenses = load_expenses()
    
    while True:
        display_menu()
        choice = input("Choose (1-7): ")
        
        if choice == "7":
            print("Goodbye bro")
            break
            

main()