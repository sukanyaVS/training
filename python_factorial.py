def find_factorial(number):
    if(number < 0):
        print("Negative numbers do not have factorial")
        return
    elif(number == 0 or number == 1):
        factorial = 1
    
    else:
        factorial = 1
        for i in range(1,number+1):
           factorial = factorial * i

    print("Factorial of",number,"is",factorial)


x = int(input("Enter a number: "))
find_factorial(x)