"""
Personal Expense Tracker: A command-line application for managing personal expenses.

Available Features:
- Add, view, filter, and delete expenses
- View total spending by category
- Monthly spending summaries
- Persistent JSON storage
- Pagination for viewing and deleting expenses
"""


import json
import os       
from datetime import datetime 
import math

#Constants
CATEGORIES = ["Food", "Transport", "Home Bills", "Shopping", "Health", "Others"] 
DATA_FILE = "expenses.json"

#Display Functions

def display_menu(): 
    """Display the main menu options."""
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

#Data Persistence Functions 
  
def load_expenses():
    """Load expenses from the JSON data file.

    Returns:
        list: List of expense dictionaries, or empty list if file doesn't exist.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as file:
            return json.load(file)
    return []
    
def save_expenses(expenses):
    """Save expenses to the JSON data file.

    Args:
        expenses (list): List of expense dictionaries to save.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=2)
        
def get_date():
    """Get a valid date from the user.

    Returns:
        str: Date in YYYY-MM-DD format. Defaults to today if user presses Enter.
    """
    today = datetime.today().strftime("%Y-%m-%d")
    
    while True:
        date = input("Please input the date in YYYY-MM-DD format (Press enter for today): ")
        if date == "":
            return today
    
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date formatting, please try again...\n")
            continue

#Feature Functions for Main Menu
            
def add_expenses(expenses):
    """Add a new expense to the list.

    Prompts user for amount, category, description, and date.
    Saves the expense to JSON file.

    Args:
        expenses (list): The current list of expenses (modified in place).
    """
    print("\nLets add expenses")
            
    while True:
        try:
            amount = float(input("Enter amount(HK$): "))
            if amount <= 0:
                print("Amount must be more than 0\n")
                continue
        except ValueError:
            print("Enter a valid number...\n")
            continue
            
        print("\nCategories:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}. {cat}")
            
        while True:
            try:
                cat_choice = int(input("\nSelect category(1-6): "))
                if 1 <= cat_choice <= 6:
                    category = CATEGORIES[cat_choice - 1]
                    break
                print("Choose a number from 1 to 6")
            except ValueError:
                print("Choice must be a number")
            
        description = input("Enter a description (Optional): ")
            
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
        input("\nPress Enter to continue...")
        break

def paginated_expenses(expenses):
    """Display expenses with pagination (10 per page).

    Args:
        expenses (list): List of expenses to display.
    """
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
            while True:
                user_input = input("\nPress Enter for next page, or 'q' to exit: ")
                if user_input.lower() == 'q':
                    return
                elif user_input == "":
                    page += 1
                    loop = 0
                    break
                else:
                    print("Please either press enter or type 'd'...")
                    continue
                
def total_spent(expenses):
    """Display total spending summary by category.

    Args:
        expenses (list): List of expenses to summarize.
    """
    if not expenses:
        print("\n No expenses yet")
    else: 
        categories = {cat: 0 for cat in CATEGORIES}
        total = 0
                    
        for expense in expenses:
            categories[expense["category"]] += expense["amount"]
            total += expense["amount"]
                    
        print(f"\n{'='*40}")
        print(f"Total Spending Summary")
        print(f"{'='*40}")

        for cat, amount in categories.items():
            if amount > 0:
                print(f"{cat:<15} ${amount:>10.2f}")

        print(f"{'-'*40}")
        print(f"{'TOTAL':<15} ${total:>10.2f}")
        print(f"{'='*40}")
                
        input("\nPress Enter to continue...")

def filtered_expenses(expenses): 
    """Filter and display expenses by category.

    Args:
        expenses (list): List of expenses to filter.
    """ 
    print("\nCategories:")
            
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
                
    while True:
        try:
            filter_category = int(input("Please select which category you want to filter by(1-6): ")) 
                              
            if 1 <= filter_category <= 6:
                print(f"\n--- {CATEGORIES[filter_category - 1]} expenses ---")  
                print(f"{'ID':<4} {'Date':<12} {'Amount':<10} {'Description'}")
                        
                found = False
                for dictionary in expenses:
                    if dictionary['category'] == CATEGORIES[filter_category - 1]:
                            found = True
                            print(f"{dictionary['id']:<4} {dictionary['date']:<12} {dictionary['amount']:<10.2f} {dictionary['description']} ")
                if not found:
                    print(f"No expenses found in {CATEGORIES[filter_category - 1]}")
                input("\nPress Enter to continue...")
                break  
            else:         
                print("please input a number from 1 to 6\n")
                    
        except ValueError:
            print("Please type in a number\n")

def delete_expense(expenses):
    """Delete an expense by ID with paginated view.

    Shows expenses page by page, allows user to select an expense to delete.

    Args:
        expenses (list): List of expenses (modified in place).
    """
    if not expenses:
        print("\nNo expenses to delete")
    else:
        page = 1
        loop = 0
        total_page = math.ceil(len(expenses)/10)
        delete_condition = False
                
        for i, expense in enumerate(expenses,1):
            if loop == 0:
                start_num = (page - 1) * 10 + 1
                end_num = min(page * 10, len(expenses))
                print(f"\n--- Current Expenses (Page {page}/{total_page}) ---")
                print(f"{'ID':<4} {'Date':<12} {'Amount':<10} {'Description'}")
                        
            print(f"{expense['id']:<4} {expense['date']:<12} {expense['amount']:<10.2f} {expense['description']} ")
            loop += 1
                    
            if (i % 10) == 0 and i != len(expenses):
                while True:
                    user_input = input("\nPress Enter for next page, or 'd' to select an expense to delete: ")
                    if user_input.lower() == 'd':
                        delete_condition = True
                        break
                    elif user_input == "":
                        page += 1
                        loop = 0
                        break
                    else:
                        print("Please either press enter or type 'd'...")
                        continue
                if delete_condition:
                    break
                    
                            
        if not delete_condition and expenses:
            while True:
                user_input = input("\nPress 'd' to delete an expense, or Enter to return to main menu: ")
                if user_input.lower() == 'd':
                    delete_condition = True
                    break
                elif user_input == "":
                    break
                else:
                    print("Please either press enter or type 'd'...")
                            
        if delete_condition:
            while True:
                try:
                    id_delete = int(input("Enter ID to delete (or 0 to cancel): "))
                    if id_delete == 0:
                        print("Operation cancelled")
                        break
                    
                    found = False
                    for idx, exp in enumerate(expenses):
                        if exp["id"] == id_delete:
                            deleted_amount = exp["amount"]
                            deleted_category = exp["category"]
                            expenses.pop(idx)
                            save_expenses(expenses)
                            print(f"✅ Deleted: ${deleted_amount} for {deleted_category}")
                            found = True
                            break
                    
                    if not found:
                        print("ID not found...")
                        continue
                    break
                    
                except ValueError:
                    print("Only integers are allowed")
        
        if delete_condition:                   
            input("\nPress Enter to continue...")
        
def monthly_summary(expenses):
    """Display spending summary for a specific month.

    Args:
        expenses (list): List of expenses to summarize.
    """
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
                    
            categories = {cat: 0 for cat in CATEGORIES}
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
                
            input("\nPress Enter to continue...")
            break
                      
        except ValueError:
            print("Please type in YYYY-MM format")

#Main Program
     
def main():
    """Main program entry point. Handles menu navigation."""
    expenses = load_expenses()
    while True:
        display_menu()
        choice = input("Choose (1-7): ")
        
        if choice == "1":
            add_expenses(expenses)
    
        elif choice == "2":
            if not expenses:
                print("\nNo expenses yet...")
                input("Press Enter to continue...")
            else:
                paginated_expenses(expenses)
                input("\nPress Enter to continue...")

        elif choice == "3":
           total_spent(expenses) 
                       
        elif choice == "4":
            filtered_expenses(expenses)
         
        elif choice == "5":
            delete_expense(expenses)
                 
        elif choice == "6":
           monthly_summary(expenses)
               
        elif choice == "7":
            print("\nGoodbye.")
            break   
        
        else:
            print("Input a number from 1 to 7")   
            input("Press enter to continue...") 
                              
if __name__ == "__main__":
    main()