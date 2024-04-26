from bank import Bank
from person import Admin


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