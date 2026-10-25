class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    # Deposit method returns the amount deposited after updating balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return amount
        return 0

    # Withdraw method checks for sufficient balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    # Print current balance
    def check_balance(self):
        print(f"Current Balance: KSh {self.balance:,.2f}")

    # Print customer details
    def customer_details(self):
        print("--- Customer Details ---")
        print(f"Customer Name   : {self.customer_name}")
        print(f"Account Number  : {self.account_number}")
        print(f"Date of Opening : {self.date_of_opening}")
        print(f"Balance         : KSh {self.balance:,.2f}")


# Usage Demonstration:
account = BankAccount("ACC1001", 15000.0, "2026-01-15", "Sarah Connor")

# Test methods
account.customer_details()
print("\nDeposited:", account.deposit(5000))
account.check_balance()

print("\nWithdrawal Attempt (6000):", account.withdraw(6000))
account.check_balance()

print("\nWithdrawal Attempt (20000):", account.withdraw(20000))
