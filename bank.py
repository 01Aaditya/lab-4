import os
from datetime import datetime

CUSTOMER_FILE = "customers.txt"
TRANSACTION_FILE = "transactions.txt"


def load_customers():
    """Load customers from file into a dictionary {account: [name, balance]}"""
    customers = {}
    if os.path.exists(CUSTOMER_FILE):
        with open(CUSTOMER_FILE, "r") as f:
            for line in f:
                try:
                    acc, name, balance = line.strip().split(",")
                    customers[acc] = [name, float(balance)]
                except ValueError:
                    continue  # skip invalid lines
    return customers


def save_customers(customers):
    """Save customers back to file"""
    with open(CUSTOMER_FILE, "w") as f:
        for acc, (name, balance) in customers.items():
            f.write(f"{acc},{name},{balance}\n")


def log_transaction(account, action, amount, status="SUCCESS"):
    """Log all transactions into a separate file"""
    with open(TRANSACTION_FILE, "a") as f:
        f.write(f"{datetime.now()} | {account} | {action} | {amount} | {status}\n")


def add_customer(customers, account, name, balance=0.0):
    if account in customers:
        print("⚠️ Account already exists.")
        return
    customers[account] = [name, float(balance)]
    save_customers(customers)
    print("✅ Customer added successfully.")


def deposit(customers, account, amount):
    try:
        if account not in customers:
            raise KeyError("Account not found.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        customers[account][1] += amount
        save_customers(customers)
        log_transaction(account, "DEPOSIT", amount)
        print(f"✅ Deposited {amount}. New Balance: {customers[account][1]}")

    except Exception as e:
        log_transaction(account, "DEPOSIT", amount, status=f"FAILED ({e})")
        print(f"❌ Error: {e}")


def withdraw(customers, account, amount):
    try:
        if account not in customers:
            raise KeyError("Account not found.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if customers[account][1] < amount:
            raise ValueError("Insufficient balance.")

        customers[account][1] -= amount
        save_customers(customers)
        log_transaction(account, "WITHDRAW", amount)
        print(f"✅ Withdrawn {amount}. New Balance: {customers[account][1]}")

    except Exception as e:
        log_transaction(account, "WITHDRAW", amount, status=f"FAILED ({e})")
        print(f"❌ Error: {e}")


def view_balance(customers, account):
    try:
        if account not in customers:
            raise KeyError("Account not found.")
        print(f"💰 Balance for {customers[account][0]}: {customers[account][1]}")
    except Exception as e:
        print(f"❌ Error: {e}")


# CLI Menu
def main():
    customers = load_customers()
    while True:
        print("\n===== Simple Banking System =====")
        print("1. Add Customer")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Balance")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            acc = input("Enter account number: ")
            name = input("Enter customer name: ")
            bal = float(input("Enter initial balance: "))
            add_customer(customers, acc, name, bal)

        elif choice == "2":
            acc = input("Enter account number: ")
            amt = float(input("Enter deposit amount: "))
            deposit(customers, acc, amt)

        elif choice == "3":
            acc = input("Enter account number: ")
            amt = float(input("Enter withdrawal amount: "))
            withdraw(customers, acc, amt)

        elif choice == "4":
            acc = input("Enter account number: ")
            view_balance(customers, acc)

        elif choice == "5":
            print("👋 Exiting. Thank you for banking with us!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
