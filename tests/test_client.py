"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
import unittest
from client.client import Client
from email_validator import EmailNotValidError

class TestClient(unittest.TestCase):

    def test_client_creation_valid(self):
        client = Client(101, "Susan", "Clark", "susan@pixell.com")
        self.assertEqual(client.client_number, 101)
        self.assertEqual(client.first_name, "Susan")
        self.assertEqual(client.last_name, "Clark")
        self.assertEqual(client.email_address, "susan@pixell.com")

    def test_client_creation_invalid_email(self):
        client = Client(102, "John", "Doe", "invalid-email")
        self.assertEqual(client.email_address, "email@pixell-river.com")

    def test_invalid_client_number(self):
        with self.assertRaises(ValueError):
            Client("abc", "Susan", "Clark", "susan@pixell.com")

    def test_invalid_first_name(self):
        with self.assertRaises(ValueError):
            Client(103, "", "Clark", "susan@pixell.com")

    def test_invalid_last_name(self):
        with self.assertRaises(ValueError):
            Client(103, "Susan", "", "susan@pixell.com")

if __name__ == '__main__':
    unittest.main()