from abc import ABC
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

            
class Bank:
    def __init__(self,name):
        self.name = name
        self.users = []
        self.loan_amount = 0
        self.loan_allowed = True

    def find_user(self,bank_account):
        try:
            item = None
            for user in self.users:
                if user.bank_account == bank_account:
                    item = user
            return item
        except AttributeError:
            print("Invalid Input")
        


    def get_loan_permission(self):
        try: 
            return self.loan_allowed
        except AttributeError:
            print("Unable to access")
    
    def set_loan_permission(self,ch):
        try:
            self.loan_allowed = ch
        except AttributeError:
            print("Invalid input")

    def add_acount(self,user):
        try:
            self.users.append(user)
        except AttributeError:
            print("Unable to access")
    

        
    def delete_account(self,bank_account):
        try: 
            item = self.find_user(bank_account)
            if item:
                self.users.remove(item)
                print(f"{item.bank_account} is successfully deleted")
            else:
                print("Account Number doesn't exixt")
        except AttributeError:
            print("Error")
            

    def all_user_show(self):
        try:
            print("Name\tAccount Number\tAccount Type\tBalance")
            for user in self.users:
                print(f"{user.name}\t{user.bank_account}\t{user.account_type}\t\t{user.balance}")
        except AttributeError:
            print("Error")


    def total_balance(self):
        try:
            total = 0
            for user in self.users:
                total += user.balance
            print(f"Total Balance: {total}")
        except AttributeError:
            print("Error")
    

    



    
        
    

        


def login_as_admin():
    while True:
        try:
            print("1. Create an Account")
            print("2. Delete User Account")
            print("3. See User Accounts")
            print("4. Total Available Balance")
            print("5. Total loan Amount")
            print("6. On or Off Loan Feature")
            print("7. Exit")

            ch = int(input("Enter Option: "))

            if ch == 1:
                name = input("Enter Name: ")
                password = input("Enter Password: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                age = int(input("Enter Age: "))
                address = input("Enter Address: ")
                account_type = input("Enter Account Type: ")
                admin.create_account(name,password,email,phone,age,address,account_type)
            elif ch == 2:
                account_number = input("Enter Account Number:")
                admin.delete_user_account(account_number)
            elif ch == 3:
                admin.all_user_show()
            elif ch == 4:
                admin.total_balance()
            elif ch == 5:
                print(admin.total_loan_amount())
            elif ch == 6:
                print("Enter 1 for giving loan permission and 0 for not allowing permission")
                option = input("Enter (1/0): ")
                admin.loan_allowed(option)
            elif ch == 7:
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Enter Valid input!!!")



def login_as_user(user):
    while True:
        try:
            print("1. Withdraw Amount")
            print("2. Deposit Amount")
            print("3. Available Balance")
            print("4. Transaction History")
            print("5. Loan")
            print("6. Send Money")
            print("7. Exit")

            ch = int(input("Enter Option: "))

            if ch == 1:
                amount = int(input("Enter amount: "))
                user.withdraw(amount)
            elif ch == 2:
                amount = int(input("Enter amount: "))
                user.deposite(amount)
            elif ch == 3:
                user.available_balance()
            elif ch == 4:
                user.transaction_history()
            elif ch == 5:
                amount = int(input("Enter amount: "))
                user.loan(amount)
            elif ch == 6:
                account_num = input("Enter Account Number: ")
                amount = int(input("Enter amount: "))
                user.send_money(account_num,amount)
            elif ch == 7:
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Enter Valid input!!!")
            
        

my_bank = Bank("abc bank")
admin = Admin('tawhid','1234', 'tawhid@gamil.com', '23332', 23, 'Maryland')  
admin.assign_admin(my_bank) 

# #...............For Debugging.................
# user1 = admin.create_account('tawhid','111','tawhid@gmail.com','2222',23,'Dhaka','saving')
# # user1.deposite(11500)
# user2 = admin.create_account("Sabbir", "222","user@gamil.com", '2223', 21, 'Dhaka',"saving")  

while True:
    try: 
        print("1. Login as Admin")
        print("2. Login as User")
        print("3. Exit")

        ch = int(input("Enter Option: "))

        if ch == 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if username == "admin" and password == "1234":
                print(admin)
                login_as_admin()
            else:
                print("Incorrect Username or Password!!!")
        
        elif ch == 2:
            act_num = input("Enter Account Number: ")
            password = input("Enter Password: ")
            
            user = my_bank.find_user(act_num)
            if user:
                if user.password == password:
                    print(user)
                    login_as_user(user)
                else:
                    print("Incorrect Account Number or Passoword")
            else:
                print("Not found the user")
        elif ch == 3:
            break
        else:
            print("Invalid Input!!!")
    except ValueError:
        print("Invalid Input")











#.................For Debuggin................


# login_as_admin()
# login_as_user(user1)

# admin.all_user_show()
# admin.loan_allowed(True)  
# user1.loan(10)
# print(user1.balance)