# Expense Tracker CLI

A simple command-line application to track personal expenses and manage multiple users, written in Python.

## Features
- Add untracked expenses
- Create a personal expense tracker (user)
- Add expenses to existing users
- View all untracked expenses
- View all expenses for a specific user
- Simple, interactive menu-driven interface

## Requirements
- Python 3.7 or higher

## Setup
1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
Follow the on-screen menu prompts to:
- Create a new user/tracker
- Add expenses (either untracked or to a user)
- View expenses
- Exit the application

## File Descriptions
- `main.py`: Main entry point; handles user interaction and menu logic.
- `expense.py`: Defines the `Expense` class and manages untracked expenses.
- `ExpenseTracker.py`: Defines the `ExpenseTracker` class for user-specific expense management.

## Notes
- All data is stored in memory; exiting the program will erase all expenses and users.
- No persistent storage is implemented.
- Error handling is minimal; please enter valid data as prompted.

## License
This project is for educational purposes and is not intended for production use. 