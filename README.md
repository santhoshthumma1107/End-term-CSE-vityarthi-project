# Personal Finance Manager (Tkinter)

A small Python/Tkinter desktop app to track basic personal finances: income, expenses, savings calculation and handling unexpected "accident" dues.

Author: Santhosh  
Date: 23 November 2025

## Features
- Add income and expenses (updates current balance).
- Simple savings calculator (moves a percentage of balance to savings).
- Random "accident" event that creates accident dues (bounded by current balance).
- Pay accident dues using savings first, then balance.
- Lightweight GUI built with Tkinter (no external deps).

## Requirements
- Python 3.8+ (Windows)
- No external packages required.

## Setup (Windows)
1. Open PowerShell or Command Prompt in the project folder:
   cd "c:\Users\Santhosh\OneDrive\Desktop\CSE vityarthi project"
2. (Optional) Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Run the app:
   python main.py

## Usage (UI notes)
- "Add Income": enter amount and click to increase balance.
- "Add Expense": enter amount and click to decrease balance.
- Savings percentage field defaults to 15. Click "Calculate Savings..." to move that percent from balance to savings.
- "Palm of GOD's" button triggers a random accident expense (adds to Accident_due).
- "Pay Your Accident Dues" pays dues using savings first, then balance.
- Labels show Current Balance, Savings Calculator, and Accident_due.

## Known Issues / Limitations
- No persistence (state is in-memory; data lost on exit).
- Minimal input validation — non-numeric input will raise exceptions.
- Negative balances are possible.
- Global state and single-file structure reduce testability and maintainability.

## Recommended Improvements
- Add input validation and user-friendly error messages.
- Persist transactions/state (SQLite or JSON).
- Refactor business logic into testable modules/classes.
- Add transaction history, export (CSV), charts, and unit tests (pytest).
- Improve UI layout and accessibility.

## Testing
- Manual test cases:
  - Add income and verify balance increments correctly.
  - Add expense greater than balance and observe behavior.
  - Calculate savings with several percentages.
  - Trigger multiple accidents and pay dues.
- For automated tests: extract core logic into a FinanceState class/module and write pytest unit tests for add_income, add_expense, calculate_savings, apply_accident, pay_dues.

## Screenshots
Place screenshots in an `images/` folder and reference them in slides or this README:
- images/screen_start.png
- images/after_income.png
- images/after_savings.png
- images/after_accident.png
- images/after_pay_dues.png

## Project Structure
- main.py — main application (Tkinter UI + logic)
- README.md — this file
- images/ — optional screenshots