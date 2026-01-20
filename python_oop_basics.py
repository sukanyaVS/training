class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display(self):
        print("Account number :", self.acc_no)
        print("Account holder name :", self.name)
        print("Account balance :", self.balance)
        print("========================")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        print("Account balance after deposit :" ,self.balance)    

    def withdraw(self, amount):
        if amount <= 0:
         print("Invalid withdraw amount")
        elif amount > self.balance:
         print("Insufficient balance") 
        else:
         self.balance -= amount 
         print("Account balance after withdrawel :" ,self.balance) 

obj1 = BankAccount(1234, 'Sukanya', 15000)
obj1.display()
obj1.deposit(1000)
obj1.withdraw(2000)
