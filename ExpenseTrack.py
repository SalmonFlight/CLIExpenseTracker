import json
import os
from datetime import datetime 

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
            print()
            
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
            print("To be added")
        
        elif choice == "7":
            print("Goodbye.")
            break   
        
        else:
            print("Input a number from 1 to 7")    
                
                
     
                        
                
        

            

main()