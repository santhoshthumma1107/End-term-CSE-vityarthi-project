# Project Statement

## Problem statement
Many users need a lightweight, easy-to-use desktop tool to record and track basic personal finances (income, expenses, savings) and handle unexpected expenses. Existing tools can be complex or require online accounts; a simple offline utility is required to quickly record transactions, auto-allocate savings, and manage occasional unplanned dues.

## Scope of the project
- Provide a local, single-user desktop application (Tkinter) for basic personal finance tracking.
- Support adding income and expenses, calculating and moving a configurable percentage to savings, generating and tracking random unexpected dues (accidents), and paying those dues using savings and/or balance.
- Keep state in memory for the prototype; optional future persistence (JSON/SQLite).
- Focus on core functionality and simple UI; not intended as a full accounting package (no multi-user support, no tax computations, no advanced reporting in the initial version).

## Target users
- Students and individual users who want a minimal offline tool to manage day-to-day personal finances.
- Beginners learning Python/Tkinter who want a demonstrative finance app.
- Users who prefer a simple local utility without cloud sync or sign-ins.

## High-level features
- Add Income: enter amount to increase current balance.
- Add Expense: enter amount to decrease current balance.
- Savings Calculator: move a configurable percentage of balance to a savings pool.
- Random Accident Event: generate an unexpected expense (bounded by current balance) recorded as accident dues.
- Pay Accident Dues: settle dues using savings first, then balance if needed.
- Real-time UI feedback: labels show Current Balance, Savings, and Accident Dues.
- Prototype constraints: in-memory state, minimal input validation, single-file implementation.