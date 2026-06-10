import json
import os
import datetime 

today = datetime.today().strftime("%Y-%m-%d")

def load_expenses():
    if os.path.exists("expenses.json"):
        with open("expenses.json") as file:
            return json.load(file)
    return []
    
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)
        
def get_date():
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
    print()