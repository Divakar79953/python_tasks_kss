# Bank Account

class BankAccount:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount Deposited:",amount)

    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance=self.balance-amount
            print("Amount Withdrawan:",amount)

        else:
            print("Insufficient Balance")

    def display_balance(self):
         print("Customer Name:",self.name)
         print("Account Number:",self.account_number)
         print("Current Balance:",self.balance)

customer1=BankAccount("Divakar Naidu",7995312753,70000)
customer1.deposit(700)
customer1.withdraw(57000)
customer1.display_balance()
