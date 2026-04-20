import os

class ExpenseTracker:
    def __init__(self, filename="expenses.txt"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()
    
    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    try:
                        amount = float(line.strip())
                        self.expenses.append(amount)
                    except ValueError:
                        pass

    def save_expenses(self):
        with open(self.filename, "w") as file:
            for amount in self.expenses:
                file.write(f"{amount}\n")
    
    def add_expense(self, amount):
        self.expenses.append(amount)

    def show_summary(self):
        if not self.expenses:
            print("No expenses recorded!")
            return

        total = sum(self.expenses)
        average = total / len(self.expenses)

        print("\n--- Summary ---")
        print("Total:", total)
        print("Average:", average)


def main():
    tracker = ExpenseTracker()

    while True:
        user_input = input("Enter expense (or 'done' to finish): ")

        if user_input == "done":
            break

        try:
            amount = float(user_input)
            tracker.add_expense(amount)
            print("Added!")
        except ValueError:
            print("Invalid number!")

    tracker.save_expenses()
    tracker.show_summary()


main()
