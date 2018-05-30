class Account:
    def __init__(self, balance=0, account_type='checking'):
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount
