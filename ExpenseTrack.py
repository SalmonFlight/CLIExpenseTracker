import json
import os
from datetime import datetime 
import math 

def display_menu():
    print()
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
        
        if choice == "1":
            print("\nLets add expenses")
            
            while True:
                try:
                    amount = float(input("Enter amount(HK$): "))
                    if amount <= 0:
                        print("Amount must be more than 0")
                        continue
                    else:
                        break
                except ValueError:
                    print("Enter a valid number")
            
            categories = ["Food", "Transport", "Home Bills", "Shopping", "Health", "Others"]
            print("\nCategories:")
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")
            
            while True:
                try:
                    cat_choice = int(input("Select category(1-6): "))
                    if 1 <= cat_choice <= 6:
                        category = categories[cat_choice - 1]
                        break
                    print("Choose a number from 1 to 6")
                except ValueError:
                    print("Choice must be a number")
            
            description = input("Enter a description(Optional): ")
            
            date = get_date()
            
            expense = {
                "id" : len(expenses) + 1,
                "amount" : amount,
                "category" : category,
                "description" : description,
                "date" : date
            }    
            
            expenses.append(expense)
            save_expenses(expenses)
            
            print(f"Added {amount}HK$ for {category} on {date}")
            input("\nPress enter to continue...")
    
        elif choice == "2":
            if not expenses:
                print("\nNo expenses yet...")
                input("Press enter to continue")
            else:
                page = 1
                loop = 0
                total_page = math.ceil(len(expenses)/10)
                    
                for i, expense in enumerate(expenses,1):
                    if loop == 0:
                        start_num = (page - 1) * 10 + 1
                        end_num = min(page * 10, len(expenses))
                        print(f"\nPage {page}/{total_page} expenses ({start_num}-{end_num}):")
                        print(f"{'ID':<4} {'Date':<12} {'Amount':<10} {'Description'}")
                        
                    print(f"{expense['id']:<4} {expense['date']:<12} {expense['amount']:<10.2f} {expense['description']} ")
                    loop += 1
                    
                    if (i % 10) == 0 and i != len(expenses):
                        user_input = input("\nPress Enter for next page, or 'q' to exit: ")
                        if user_input.lower() == 'q':
                            break
                        else:
                            page += 1
                            loop = 0
                input("\nPress Enter to continue...")

        elif choice == "3":
            if not expenses:
                print("\n No expenses yet")
            else:
                total = 0 
                for dictionary in expenses:
                    total += dictionary['amount']
                print(f"\nYou have spent a total of {total}")
            input("\nPress enter to continue...")
            
        elif choice == "4":
            categories = ["Food", "Transport", "Home Bills", "Shopping", "Health", "Others"]
            
            print("\nCategories:")
            
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")
                
            while True:
                try:
                    filter_category = int(input("Please select which category you want to filter by(1-6):")) 
                              
                    if 1 <= filter_category <= 6:
                        print(f"\n--- {categories[filter_category - 1]} expenses ---")  
                        print(f"{'ID':<4} {'Date':<12} {'Amount':<10} {'Description'}")
                        
                        found = False
                        for dictionary in expenses:
                            if dictionary['category'] == categories[filter_category - 1]:
                                found = True
                                print(f"{dictionary['id']:<4} {dictionary['date']:<12} {dictionary['amount']:<10.2f} {dictionary['description']} ")
                        if not found:
                            print(f"No expenses found in {categories[filter_category - 1]}")
                        input("\nPress enter to continue...")
                        break           
                    print("please input a number from 1 to 6")
                    
                except ValueError:
                    print("Please type in a number")
         
        elif choice == "5":
            print("To be added")
        
        elif choice == "6":
            while True:
                try:
                    month = input("\nEnter month (YYYY-MM) (press enter to use the current month and year): ")
                    
                    if month == "":
                        current_year = datetime.today().year
                        current_month = datetime.today().month
                        month = f"{current_year}-{current_month:02d}"
                
                    if len(month) != 7 or month[4] != "-":
                        print("Please type in YYYY-MM format")
                        continue
                    
                    year_num = int(month[0:4])
                    if year_num < 1900 or year_num > 2100:
                        print("Please input a valid year (1900-2100)")
                        continue
                    
                    month_num = int(month[5:7])
                    if month_num > 12 or month_num < 1:
                        print("Please input a valid month (1-12)")
                        continue
                    
                    categories = {"Food" : 0, "Transport" : 0, "Home Bills" : 0, "Shopping" : 0, "Health" : 0, "Others" : 0}
                    total = 0
                    
                    for expense in expenses:
                        if expense["date"].startswith(month):
                            if expense["category"] in categories:
                                categories[expense["category"]] += expense["amount"]
                                total += expense["amount"]
                    
                    print(f"\n{'='*40}")
                    print(f"Monthly Summary: {month}")
                    print(f"{'='*40}")

                    for cat, amount in categories.items():
                        if amount > 0:
                            print(f"{cat:<15} ${amount:>10.2f}")

                    print(f"{'-'*40}")
                    print(f"{'TOTAL':<15} ${total:>10.2f}")
                    print(f"{'='*40}")
                
                    input("\nPress enter to continue")
                    break
                      
                except ValueError:
                    print("Please type in YYYY-MM format")
               
        elif choice == "7":
            print("\nGoodbye.")
            break   
        
        else:
            print("Input a number from 1 to 7")    
                
                
main()