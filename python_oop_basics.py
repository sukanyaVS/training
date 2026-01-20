class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance

    def display(self):
        print("Account number :", self.acc_no)
        print("Account holder name :", self.name)
        print("Account balance :", self.__balance)
        print("========================")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        print("Account balance after deposit :" ,self.__balance)    

    def withdraw(self, amount):
        if amount <= 0:
         print("Invalid withdraw amount")
        elif amount > self.__balance:
         print("Insufficient balance") 
        else:
         self.__balance -= amount 
         print("Account balance after withdrawel :" ,self.__balance) 

obj1 = BankAccount(1234, 'Sukanya', 15000)
obj1.display()
obj1.deposit(1000)
obj1.withdraw(2000)
