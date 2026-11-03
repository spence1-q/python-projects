# i. Create a parent class named Account
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # ii. Include a method named displayAccount()
    def displayAccount(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:,.2f}")


# iii. & iv. Create a child class named SavingsAccount that inherits from Account and adds interest rate
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    # v. Include a method named calculateInterest() using: Interest = Balance × Interest Rate / 100
    def calculateInterest(self):
        return (self.balance * self.interest_rate) / 100

    # Optional display method to fulfill vi cleanly
    def displaySavingsDetails(self):
        self.displayAccount()
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Calculated Interest: {self.calculateInterest():,.2f}")


# vi. Create a SavingsAccount object and display the account details and calculated interest
if __name__ == "__main__":
    my_savings = SavingsAccount(account_number="ACC-93890", balance=50000.00, interest_rate=5.5)
    
    print("--- Savings Account Details ---")
    my_savings.displaySavingsDetails()
