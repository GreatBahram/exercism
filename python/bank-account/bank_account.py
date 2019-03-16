import threading


class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False
        self.__lock = threading.Lock()

    def get_balance(self):
        if not self.is_open:
            raise ValueError('First open the account, please.')
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError('You cannot reopen an open account.')
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('First open the account.')
        if amount < 0:
            raise ValueError('Deposit cannot be negative.')
        with self.__lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('First open the account, please.')
        if amount < 0:
            raise ValueError('Invalid withdraw amount, it cannot be negative.')
        if self.balance < amount:
            raise ValueError('Insufficient balance.')
        with self.__lock:
            self.balance -= amount

    def close(self):
        if not self.is_open:
            raise ValueError('You cannot re-close a close account.')
        self.is_open = False
        self.balance = 0
