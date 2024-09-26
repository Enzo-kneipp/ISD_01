"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_bank_account_creation_valid(self):
        account = BankAccount(20019, 101, 100.0)
        self.assertEqual(account.account_number, 20019)
        self.assertEqual(account.client_number, 101)
        self.assertEqual(round(account.balance, 2), 100.00)

    def test_bank_account_creation_invalid_account_number(self):
        with self.assertRaises(ValueError):
            BankAccount("abc", 101)

    def test_bank_account_creation_invalid_client_number(self):
        with self.assertRaises(ValueError):
            BankAccount(20019, "xyz")

    def test_deposit(self):
        account = BankAccount(20019, 101, 100.0)
        account.deposit(50.0)
        self.assertEqual(round(account.balance, 2), 150.00)

    def test_invalid_deposit_amount(self):
        account = BankAccount(20019, 101, 100.0)
        with self.assertRaises(ValueError):
            account.deposit(-50.0)

    def test_withdraw(self):
        account = BankAccount(20019, 101, 100.0)
        account.withdraw(50.0)
        self.assertEqual(round(account.balance, 2), 50.00)

    def test_invalid_withdraw_amount(self):
        account = BankAccount(20019, 101, 100.0)
        with self.assertRaises(ValueError):
            account.withdraw(150.0)

if __name__ == '__main__':
    unittest.main()