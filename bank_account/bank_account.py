"""
Description: BankAccount class for managing account operations.
Author: ACE Faculty
Edited by: Enzo Kneipp (enzo@example.com)
Date: 2024-09-26
"""

class BankAccount:
    def __init__(self, account_number, client_number, balance):
        """Initialize a BankAccount with account number, client number, and balance."""
        if not isinstance(balance, (float, int)):
            raise ValueError("Balance must be a float or integer")
        self.account_number = account_number
        self.client_number = client_number
        self.balance = float(balance)

    def deposit(self, amount):
        """Deposit a valid amount to the account."""
        if not isinstance(amount, (float, int)):
            raise ValueError("Deposit must be a numeric value")
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw a valid amount from the account."""
        if not isinstance(amount, (float, int)):
            raise ValueError("Withdrawal must be a numeric value")
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def __str__(self):
        """Return a string representation of the BankAccount."""
        return f"BankAccount(account_number={self.account_number}, balance={self.balance})"
