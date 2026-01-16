def countNumbers(*numbers):
    if(len(numbers) == 0):
        print("There is no numbers")
        return
    
    countOfOddNumbers = 0
    countOfEvenNumbers = 0
    
    for i in numbers:
        if(i%2 == 0):
            countOfEvenNumbers += 1
        else:
            countOfOddNumbers += 1

    print("Count of even numbers : ", countOfEvenNumbers , end="  and ")
    print("Count of odd numbers : ", countOfOddNumbers)     

countNumbers()
countNumbers(2,4,8,12)
countNumbers(1,3,5)
countNumbers(1,2,34,4,5,6,7)
