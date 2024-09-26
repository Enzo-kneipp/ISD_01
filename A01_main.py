"""
Description: A client program written to verify the correctness of 
the BankAccount and Transaction classes.
Author: ACE Faculty
Edited by: Enzo Kneipp (enzo@example.com)
Date: 2024-09-26
"""
from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods in the BankAccount class."""
    
    try:
        # 1. Create a valid Client instance with unique values
        client = Client(1001, "Enzo Kneipp", "enzo@example.com")
        
        # 2. Declare a BankAccount object
        bank_account = None

        # 3. Instantiate BankAccount using client details and a valid balance
        bank_account = BankAccount(12345, client.client_number, 1000.0)

        # 4. Attempt to create a BankAccount with an invalid balance
        try:
            invalid_account = BankAccount(54321, client.client_number, "invalid_balance")
        except ValueError as e:
            print(f"Error: {e}")

        # 5. Print the Client and BankAccount instances
        print(client)
        print(bank_account)

        # 6. Attempt to deposit a non-numeric value
        try:
            bank_account.deposit("invalid_deposit")
        except ValueError as e:
            print(f"Error: {e}")

        # 7. Attempt to deposit a negative value
        try:
            bank_account.deposit(-100)
        except ValueError as e:
            print(f"Error: {e}")

        # 8. Withdraw a valid amount
        bank_account.withdraw(100)

        # 9. Attempt to withdraw a non-numeric value
        try:
            bank_account.withdraw("invalid_withdrawal")
        except ValueError as e:
            print(f"Error: {e}")

        # 10. Attempt to withdraw a negative value
        try:
            bank_account.withdraw(-50)
        except ValueError as e:
            print(f"Error: {e}")

        # 11. Attempt to withdraw more than the balance
        try:
            bank_account.withdraw(10000)
        except ValueError as e:
            print(f"Error: {e}")

        # 12. Print the final state of BankAccount
        print(bank_account)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
