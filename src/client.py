from src.account import Account


class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, balance, account_type):
        bonus = 10
        a = Account(balance + bonus, account_type)
        self.accounts.append(a)
