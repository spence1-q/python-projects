class BankAccount:
    def __init__(self):
        self.account_number = ""
        self.customer_name = ""
        self.balance = 0.0

    def setAccountDetails(self, acc_num, name, initial_balance=0.0):
        self.account_number = acc_num
        self.customer_name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited KSh {amount:,.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew KSh {amount:,.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def displayAccount(self):
        print("\n--- Bank Account Details ---")
        print(f"Account Number : {self.account_number}")
        print(f"Customer Name  : {self.customer_name}")
        print(f"Current Balance: KSh {self.balance:,.2f}")

# Main 
if __name__ == "__main__":
    # Create an object of the BankAccount class
    account = BankAccount()
    
    # Assign account details
    account.setAccountDetails("ACC10023", "Alice Mwangi", 5000.0)
    
    # Deposit KSh 5,000
    account.deposit(5000)
    
    # Withdraw KSh 2,000
    account.withdraw(2000)
    
    # Display the account details and updated balance
    account.displayAccount()
