class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 
        BankAccount.accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:    
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

checking = BankAccount(.01, 50000)
savings = BankAccount(.03, 10000)

checking.deposit(1500).deposit(1500).deposit(1500).withdraw(3000).yield_interest().display_account_info()
savings.deposit(150).deposit(150).deposit(150).withdraw(1000).yield_interest().display_account_info()

BankAccount.print_all_accounts()