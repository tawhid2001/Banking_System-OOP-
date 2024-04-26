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
    

    



    

