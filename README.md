Banking System
This project implements a basic banking system with functionalities for both admins and users. It allows admins to create and manage user accounts, view account balances, and grant or deny loan permissions. Users can perform transactions such as depositing and withdrawing money, checking their balance, viewing transaction history, applying for loans, and sending money to other accounts.

Files
bank.py: Contains the implementation of the Bank class, which manages user accounts, loan permissions, and total balances.
person.py: Defines the Person class as an abstract base class and provides concrete implementations for User and Admin subclasses. Users can perform banking operations, while Admins have additional privileges like creating user accounts and managing the system.
main.py: Implements the main program logic for user interaction. It allows users to log in as either admins or regular users, perform banking operations, and exit the program.
