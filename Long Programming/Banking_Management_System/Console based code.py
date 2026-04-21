class Customer:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}"


class Account:
    account_counter = 1000

    def __init__(self, customer):
        Account.account_counter += 1
        self.account_number = Account.account_counter
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_account(self):
        print(f"\nAccount No: {self.account_number}")
        print(self.customer.display())
        print(f"Balance: ₹{self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, age, phone):
        customer = Customer(name, age, phone)
        account = Account(customer)
        self.accounts[account.account_number] = account
        print(f"\nAccount created successfully! Account Number: {account.account_number}")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def delete_account(self, acc_no):
        if acc_no in self.accounts:
            del self.accounts[acc_no]
            print("Account deleted successfully.")
        else:
            print("Account not found.")

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            for acc in self.accounts.values():
                acc.display_account()


class Manager:
    def __init__(self, bank):
        self.bank = bank

    def menu(self):
        while True:
            print("\n--- Manager Menu ---")
            print("1. View All Accounts")
            print("2. Delete Account")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.bank.show_all_accounts()

            elif choice == "2":
                acc_no = int(input("Enter Account Number: "))
                self.bank.delete_account(acc_no)

            elif choice == "3":
                break

            else:
                print("Invalid choice!")


def customer_menu(bank):
    while True:
        print("\n--- Customer Menu ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            phone = input("Enter phone: ")
            bank.create_account(name, age, phone)

        elif choice in ["2", "3", "4"]:
            acc_no = int(input("Enter Account Number: "))
            account = bank.get_account(acc_no)

            if not account:
                print("Account not found!")
                continue

            if choice == "2":
                amount = float(input("Enter amount: "))
                account.deposit(amount)

            elif choice == "3":
                amount = float(input("Enter amount: "))
                account.withdraw(amount)

            elif choice == "4":
                account.check_balance()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")


def main():
    bank = Bank()
    manager = Manager(bank)

    while True:
        print("\n===== BANK SYSTEM =====")
        print("1. Customer")
        print("2. Manager")
        print("3. Exit")

        role = input("Select role: ")

        if role == "1":
            customer_menu(bank)

        elif role == "2":
            manager.menu()

        elif role == "3":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()