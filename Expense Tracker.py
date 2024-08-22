import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Total expense amount
        self.total_expense = 0.0

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Entry fields for adding expenses
        tk.Label(self.root, text="Type:").grid(row=0, column=0, padx=10, pady=10)
        self.type_entry = tk.Entry(self.root, width=20)
        self.type_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Description:").grid(row=1, column=0, padx=10, pady=10)
        self.desc_entry = tk.Entry(self.root, width=20)
        self.desc_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Amount:").grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root, width=20)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add expense button
        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=1, padx=10, pady=10)

        # Listbox to display expenses
        self.expense_listbox = tk.Listbox(self.root, width=50, height=10)
        self.expense_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Total expense label
        self.total_label = tk.Label(self.root, text="Total Expense: $0.00")
        self.total_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Delete and Clear buttons
        self.delete_button = tk.Button(self.root, text="Delete Selected Expense", command=self.delete_expense)
        self.delete_button.grid(row=6, column=0, padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear All Expenses", command=self.clear_expenses)
        self.clear_button.grid(row=6, column=1, padx=10, pady=10)

    def add_expense(self):
        """Adds a new expense to the list."""
        expense_type = self.type_entry.get()
        description = self.desc_entry.get()
        amount = self.amount_entry.get()

        if expense_type and description and amount:
            try:
                amount = float(amount)
                self.expense_listbox.insert(tk.END, f"{expense_type}: {description} - ${amount:.2f}")
                self.total_expense += amount
                self.update_total_label()
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount!")
        else:
            messagebox.showwarning("Warning", "Please fill in all fields!")

    def delete_expense(self):
        """Deletes the selected expense."""
        selected_expense_index = self.expense_listbox.curselection()
        if selected_expense_index:
            expense = self.expense_listbox.get(selected_expense_index)
            amount = float(expense.split('- $')[-1])
            self.total_expense -= amount
            self.expense_listbox.delete(selected_expense_index)
            self.update_total_label()
        else:
            messagebox.showwarning("Warning", "Please select an expense to delete!")

    def clear_expenses(self):
        """Clears all expenses from the list."""
        self.expense_listbox.delete(0, tk.END)
        self.total_expense = 0.0
        self.update_total_label()

    def update_total_label(self):
        """Updates the total expense label."""
        self.total_label.config(text=f"Total Expense: ${self.total_expense:.2f}")

    def clear_entries(self):
        """Clears the input fields."""
        self.type_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
