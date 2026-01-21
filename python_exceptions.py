#Accept two numbers and perform division operation.Handle the exceptions that may 
# occur when the user input is not a number and also division by zero


def div_opr(a,b):
    try:
        result = float(a) / float(b)
        print("Result = ",result)
    except ZeroDivisionError:
        print("DIvision by zero is not allowed")
    except ValueError:
        print("Invalid numbers entered")    
        

a = input("Enter first number : ")
b = input("Enter second number : ")
div_opr(a,b)

#Write a program to accept the user age as input and calculate the year of birth.
# Define an exception to raise when user enters a negative number as age.

def find_doy(age):
     if age < 0 :
        raise Exception("Negative number not allowed")
     else:
        current_year = 2026
        birth_year = 2026 - age
        print("Birth year : ",birth_year)

try:
    age = int(input("Enter your age: "))
    find_doy(age)

except ValueError:
    print("Invalid number entered")


#Define a function that accepts as argument a string with name, and returns a string 
# in which only the first letter of the name is uppercase, whereas all letters are 
# lowercase; in otherwords, 'abhishek' becomes 'Abhishek'.If something other than a 
# string object is passed as an argument, the function should raise a TypeError.


def my_func(name):
    if not isinstance(name, str):
      raise TypeError("Not string")
    
    else:    
      return name.capitalize()

try:
    print(my_func('sukanya'))
    print(my_func(5))
    print(my_func('aDHI'))

except TypeError as error:
    print("Error:", error)



