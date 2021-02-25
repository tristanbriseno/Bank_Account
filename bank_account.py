from random import *
#imports ra ndom

def new_acc_num():
    return randrange(10000000, 99999999)
    #creates an account number



class BankAccount:

    #Provided BankAccount with attributes
    def __init__(self, full_name, routing_num, balance=0):
    
        self.full_name=full_name
        self.account_num=new_acc_num()
        self.routing_num=routing_num
        self.balance=balance



    #this is the deposit function
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited: ${amount}")



    #this is the withdraw function
    def withdraw(self, amount):
        if amount > self.balance:
            print("You have Insufficient Funds! you will be charged an overdraft fee of: $10")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Your have withdrawn: ${amount}")


    #this will return and then print your balance
    def get_balance(self):
        print(f"Your current balance is: ${self.balance}")
        return self.balance


    #interest
    def add_interest(self):
        self.balance += (self.balance*0.00083)
   


    def print_reciept(self):
        print(self.full_name)
        print(f"Acc number ending in: {str(self.account_num)[slice(3, -1)]}")
        print(f"Routing Number: {self.routing_num}")
        print(f"Current balance: ${self.balance}")



#Malachi's account
Malachi=BankAccount("Malachi R", 12345678)
Malachi.withdraw(250)
Malachi.get_balance()
Malachi.print_reciept()
print("Have a Nice day!!!")
print("")

#Mason's account
Mason=BankAccount("Mason G", 12345678, 3000)
Mason.add_interest()
Mason.print_reciept()
print("Have a Nice day!!!")
print("")

#clayton's account
Clayton=BankAccount("Clayton S", 12345678)
Clayton.deposit(47000)
Clayton.print_reciept()
print("Have a Nice day!!!")
print("")
