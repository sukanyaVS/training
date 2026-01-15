print("Welcome! Don't remove your card")
input("Enter the pin : ")
print("Select your requirement..") 
print("For balance checking enter 1")
print("To deposit money enter 2")
print("To withdraw money enter 3")
print("To exit enter 4")

balance = 5000
action = int(input("Enter the number : "))

match action:
    case 1:
        print("Your current balance is ",balance)
    case 2:
        amount = int(input("Enter the amount to deposit : "))
        print("Successfully deposited and your current balance is ", (balance + amount))
    case 3:
        amount = int(input("Enter the amount to withdraw : "))
        print("Successfully debited and your current balance is ", (balance - amount))
    case 4:
         print("Please remove your card ")
    case _:
         print("Invalid selection. Try again")      
