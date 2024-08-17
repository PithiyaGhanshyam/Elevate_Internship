import json
import os

EXPENSES_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Error: Failed to decode the expense data. Starting with an empty list.")
                return {}
    return {}

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Edit Expense")
    print("3. Delete Expense")
    print("4. View Summary")
    print("5. Exit")

def add_expense(expenses):
    try:
        category = input("Enter expense category (e.g., Food, Rent, Utilities): ").strip()
        amount = float(input("Enter expense amount: "))
        
        if amount <= 0:
            print("Error: Expense amount must be positive.")
            return
        
        if category in expenses:
            expenses[category] += amount
        else:
            expenses[category] = amount
        
        print("Expense added successfully.")
        save_choice = input("Do you want to save the updated expenses to file? (yes/no): ").strip().lower()
        if save_choice == "yes":
            save_expenses(expenses)
            print("Expenses saved successfully.")
    
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the amount.")

def edit_expense(expenses):
    category = input("Enter the category of the expense you want to edit: ").strip()
    
    if category not in expenses:
        print("Error: No expense found for this category.")
        return
    
    try:
        new_amount = float(input("Enter the new expense amount: "))
        
        if new_amount < 0:
            print("Error: Expense amount must be positive.")
            return
        
        expenses[category] = new_amount
        print("Expense updated successfully.")
        
        save_choice = input("Do you want to save the updated expenses to file? (yes/no): ").strip().lower()
        if save_choice == "yes":
            save_expenses(expenses)
            print("Expenses saved successfully.")
    
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the amount.")

def delete_expense(expenses):
    category = input("Enter the category of the expense you want to delete: ").strip()
    
    if category in expenses:
        del expenses[category]
        print(f"Expense for category '{category}' deleted successfully.")
        save_choice = input("Do you want to save the updated expenses to file? (yes/no): ").strip().lower()
        if save_choice == "yes":
            save_expenses(expenses)
            print("Expenses saved successfully.")
    else:
        print("Error: No expense found for this category.")

def view_summary(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\nExpense Summary:")
    total_expenses = sum(expenses.values())
    
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
    
    print(f"Total Expenses: ${total_expenses:.2f}")

def main():
    expenses = load_expenses()
    
    while True:
        display_menu()
        
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            edit_expense(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            view_summary(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Expenses saved. Exiting the Expense Tracker. Have a great day!")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
