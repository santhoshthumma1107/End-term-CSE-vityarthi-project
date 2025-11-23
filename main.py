import random
import tkinter as tk

bal = 0 
saving = 0
accident = 0
int(bal)
int(saving)
int(accident)

def main():
    global bal
    global saving
    global accident

    def add_income():
        global bal
        amount = int(income_entry.get())
        bal += amount
        balance_label.config(text=f'Current Balance: {bal}')
        income_entry.delete(0, tk.END)

    def add_expense():
        global bal
        amount = int(expense_entry.get())
        bal -= amount
        balance_label.config(text=f'Current Balance: {bal}')
        expense_entry.delete(0, tk.END)

    def calculate_savings():
        global bal, saving
        if bal <= 0:
            return 0
        saving1 = bal * int(saving_entry.get()) * 0.01
        if saving1 > bal:
            saving1 = bal
        bal -= saving1
        saving += saving1
        balance_label.config(text=f'Current Balance: {bal}')
        savings_label.config(text=f'Savings Calculator:{saving}')

    def random_event():
        global saving,bal,accident
        random_expense = int(random.randint(0,int(bal)))
        accident += random_expense
        accident_label.config(text=f"Accident_due : {accident}")

    def pay_accident_dues():
        global saving,bal,accident
        saving -= accident
        accident = 0
        if saving < 0:
            bal += saving
            saving = 0
        savings_label.config(text=f'Savings Calculator:{saving}')
        accident_label.config(text=f'Accident_due : {accident}')
        balance_label.config(text=f'Current Balance: {bal}')


    root = tk.Tk()
    root.title("Personal Finance Manager")

    income_lable = tk.Label(root, text="Add Income:")
    income_lable.pack()

    income_entry = tk.Entry(root)
    income_entry.pack()

    income_button = tk.Button(root, text="Add Income", command=add_income)
    income_button.pack()

    expense_label = tk.Label(root, text="Add Expense:")
    expense_label.pack()

    expense_entry = tk.Entry(root)
    expense_entry.pack()

    expense_button = tk.Button(root, text="Add Expense", command=add_expense)
    expense_button.pack()

    balance_label = tk.Label(root, text=f"Current Balance: {bal}")
    balance_label.pack()

    savings_label = tk.Label(root, text=f"Savings Calculator:{saving}")
    savings_label.pack()

    saving_entry = tk.Entry(root)
    saving_entry.insert(0, "15")
    saving_entry.pack()

    savings_button = tk.Button(root, text="Calculate Savings (Add this months's 15%)", command=calculate_savings)
    savings_button.pack()

    accident_label = tk.Label(root, text=f'Accident_due : {accident}')
    accident_label.pack()

    accident_button = tk.Button(root, text="Palm of GOD's",command=random_event)
    accident_button.pack()

    pay_dues = tk.Button(root,text="Pay Your Accident Dues",command=pay_accident_dues)
    pay_dues.pack()



    root.mainloop()

if __name__ == "__main__":
    main()

