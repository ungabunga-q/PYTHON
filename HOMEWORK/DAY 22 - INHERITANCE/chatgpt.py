"""
CHATGPT EXAMPLES

"""

# Example 1: BankAccount → SavingsAccount (with interest + transaction tracking)

print('\n Tough Single Inheritance Example 1')

class BANKACCOUNT:
    def __init__(self,account,balance=0):
        self.account = account
        self.balance = balance
        self.transactions =[]
        
    def deposit(self,amount):
        self.balance +=amount
        self.transactions.append(f"Deposited {amount}")
        
    def withdrw(self,amount):
        if amount <= self.balance:
            self.balance -=amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. Balance : {self.balance}")


class SavingsAccount(BANKACCOUNT):
    def __init__(self, account, balance=0,interest_rate=0.05):
        self.interest_rate = interest_rate
        super().__init__(account, balance)
        
    def add_interest(self):
        interest = self.balance*self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest:.2f} added.")
        

sa= SavingsAccount('SB-001',5000)
sa.deposit(1000)
sa.withdrw(3000)
sa.add_interest()
print(sa.balance)
print(sa.transactions)

# Multiple Inheritance Tough

#1.Authentication + Logger → SecureApp (method resolution order challenge)

class Authentication:
    def login(self,user):
        print(f"Authenticating {user}")
        