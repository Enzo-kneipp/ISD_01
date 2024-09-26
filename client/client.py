"""
Description: Client class to represent the client information.
Author: ACE Faculty
Edited by: Enzo Kneipp (enzo@example.com)
Date: 2024-09-26
"""

class Client:
    def __init__(self, client_number, name, email):
        """Initialize a Client with a client number, name, and email."""
        self.client_number = client_number
        self.name = name
        self.email = email

    def __str__(self):
        """Return a string representation of the Client."""
        return f"Client(client_number={self.client_number}, name={self.name}, email={self.email})"
