number = int(input("Enter a number : "))
i = 1

if number > 1:
    for i in range(2,number):
        if number % i == 0:
           print("Not prime")
           break
    else:
        print("Prime")  
         
else:
    print("Not prime")