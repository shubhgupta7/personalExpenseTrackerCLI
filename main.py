import expense
from expense import Expense
from ExpenseTracker import ExpenseTracker
import datetime
import time

def addExpense(tracked=False):
    print("\nEnter the amount ")
    a = input()
    print("Enter Category ")
    b = input()
    print("Enter Note if any")
    c = input()
    d= input("Enter date (YYYY-MM-DD): ")
    if d.strip() == "":
        d = None
    newexpense = Expense(a,b,c,d,tracked)
    print(newexpense)
    return newexpense

def addTracker():
    print("Create a user and a seperate expense tracker for yourself")
    print("Enter your name")
    name = input()
    name = name.lower()
    if ExpenseTracker.User_exists(name.lower()):
        print("User already exists, please select option 5 in main menu")
        return
    expense_tracker = ExpenseTracker(name)
    print(expense_tracker)

def show_untracked_expenses():
     return expense.Expense.show_all_expenses()

def addExpensetoExistingUser():
    name = input("Please enter your name, pre existing in the database")
    if not ExpenseTracker.User_exists(name):
        print("The user does not exist kindly create a new user first")
        return
    et = ExpenseTracker.getUser(name)
    expensiveness = addExpense(True)
    et.expenses.append(expensiveness)

def getexpensebyname():
    name = input("Enter your Name : ")
    et = ExpenseTracker.existing_user.get(name)
    if et is None:
        print("Name is not there, add to the tracker first")
        return
    elif not et.expenses:
        print("No expenses found")
        return
    else:
        for x in et.expenses:
            print(x)



def start():
    while True:
        print("Welcome to our simple expense tracker")
        print(
            "1. Do you want to create a expense tracker \n2. Do you want to add an expense?\n3.Quit Tracker \n4.Show all the untracked expenses. \n5. Add expense to an existing Tracker ?\n6.Check the expenses of a given user? ")
        choice = input()

        if choice == '3':
            print("\nExiting tracker. Goodbye!")
            return
        elif choice == '2':
            addExpense()
        elif choice == '1':
            addTracker()
        elif choice == '4':
            show_untracked_expenses()
            print("\n\n")
        elif choice == '5':
            addExpensetoExistingUser()
        elif choice == '6':
            getexpensebyname()
        else:
            print("Invalid choice. Try again.")

def main():
        start()
        print("Congratulations you are done with your testing1")




main()