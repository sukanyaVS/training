class BankAccount:
    bank_name = "State Bank of India"
    

    @staticmethod
    def is_valid_amount(amount):
       if amount > 0:
          return True
       else:
          return False
       
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance
        self.transaction_list = []

    class Transaction:
        def __init__(self, amount, transaction_type):
           self.amount = amount
           self.transaction_type = transaction_type
                 

    def display(self):
        print("Account number :", self.acc_no)
        print("Account holder name :", self.name)
        print("Account balance :", self.__balance)
        print("========================")

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.__balance += amount
            print("Account balance after deposit :" ,self.__balance)
            transaction = BankAccount.Transaction(amount, "Deposit")
            self.transaction_list.append(transaction)
        else:
           print("Invalid amount")        

    def withdraw(self, amount):
        if not BankAccount.is_valid_amount(amount):
         print("Invalid withdraw amount")
        elif amount > self.__balance:
         print("Insufficient balance") 
        else:
         self.__balance -= amount 
         print("Account balance after withdrawel :" ,self.__balance)
         transaction = BankAccount.Transaction(amount, "Withdraw")
         self.transaction_list.append(transaction)

    def display_transaction(self):
        print("Transaction List......")
        for i in self.transaction_list:
           print(i.transaction_type,':',i.amount)

obj1 = BankAccount(1234, 'Sukanya', 5000)
obj1.display()
obj1.deposit(1000)
obj1.withdraw(2000)
print(obj1.bank_name)
obj1.deposit(-1000)
obj1.display_transaction()
