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

    def get_balance(self):
      return self.__balance     


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, name, balance, interest_rate):
      super().__init__(acc_no, name, balance)
      self.interest_rate = interest_rate

    def add_interest(self):
         interest = (self.get_balance() * self.interest_rate) / 100
         total_amount = self.get_balance() + interest
         self.deposit(interest)
         print("Interest added and total amount : ", total_amount)

    def withdraw(self, amount):
        balance = self.get_balance()
        if (balance - amount) < 1000:
         print("Minimum balance Rs 1000 must be maintained.")
        else:
         super().withdraw(amount)     


obj2 = SavingsAccount(1234, 'Sukanya', 15000, 8)
obj2.display()
obj2.withdraw(14050)
