from abc import ABC
from bank import Bank

class Person(ABC):
    def __init__(self,name,password,email,phone,age,address):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone
        self.age = age
        self.address = address
        self.bank = None

class User(Person):
    def __init__(self, name,password, email, phone, age,address,my_bank):
        super().__init__(name, email,password, phone, age,address)
        self.bank_account = name+str(phone)
        self.account_type = None
        self.balance = 0
        self.deposite_history = []
        self.withdraw_history = []
        self.loan_limit = 0
        self.bank = my_bank

    def __repr__(self) -> str:
        return f"Account User: {self.name}\t"


    def set_account_type(self,account_type):
        self.account_type = account_type

    def deposite(self,amount):
        temp = self.balance
        self.deposite_history.append(amount)
        self.balance += amount
        print(f"Succussfully Deposited\nprevious balance: {temp} and Current balance: {self.balance}")
    
    def withdraw(self,amount):
        if(amount > self.balance):
            print(f"Withdrawal amount exceeded\nYour current balance is {self.balance}")
            return False
        else:
            temp = self.balance
            self.withdraw_history.append(amount)
            self.balance -= amount
            print(f"Successfully Withdrawed\nprevious balance: {temp} and Current balance: {self.balance}")
            return True
        
    def available_balance(self):
        print(f"Current Balance: {self.balance}")
    
    def transaction_history(self):
        print("Transaction History\n")
        print("Deposit History:")
        for deposit in self.deposite_history:
            print(deposit)
        print("Withdraw History:")
        for withdraw in self.withdraw_history:
            print(withdraw)

    def loan(self,amount):
        try:
            if(self.loan_limit < 2) and (self.bank.get_loan_permission()):
                self.loan_limit += 1
                self.deposite(amount)
                self.bank.loan_amount += amount
                print(f"Loan amount: {amount} is added to account ")
            else:
                if self.loan_limit == 2:
                    print("Loan limit Exceeded")
                if self.bank.get_loan_permission() == False:
                    print("Bank is bankrupt")
        except AttributeError:
            print("Enter valid input")

    def send_money(self,account_number,amount):
        try:
            reciever = None
            reciever = self.bank.find_user(account_number)

            if reciever:
                sent = self.withdraw(amount)
                if sent:
                    reciever.deposite(amount)
                    print(f"Reciever: \nName: {reciever.name}\tBalance: {amount}")
                    print(f"Sender: \nName: {self.name}\tBalance: {self.balance}")
                else:
                    print(f"Insufficient Balance in Account\nCurrent Balance: {self.balance}")
                    print(f"Sender Name: {self.name}")
            else:
                print("User not found")
        except ArithmeticError:
            print("Error for invalid input")

    
class Admin(Person):
    def __init__(self, name,password, email, phone, age, address):
        super().__init__(name,password, email, phone, age, address)
        self.bank = None

    def __repr__(self) -> str:
        return f"Admin User: {self.name}"

    def assign_admin(self,my_bank):
        self.bank = my_bank
    
    def create_account(self,name,password,email,phone,age,address,account_type):
        user = User(name,email,password,phone,age,address,self.bank)
        user.set_account_type(account_type)
        Bank.add_acount(self.bank,user)
        return user

    
    def delete_user_account(self,account_number):
        Bank.delete_account(self.bank,account_number)

    def all_user_show(self):
        Bank.all_user_show(self.bank)

    def total_balance(self):
        Bank.total_balance(self.bank)

    def total_loan_amount(self):
        try:
            amount = self.bank.loan_amount
            return amount
        except AttributeError:
            print("Can not access")
    
    def loan_allowed(self,ch):
        try:
            if ch == 1:
                Bank.set_loan_permission(self.bank,1)
            else:
                Bank.set_loan_permission(self.bank,0)
        except AttributeError:
            print("Invalid Input!!!")
        
    



        