def findLargest(*numbers):
    if(len(numbers) == 0):
        print("There is no numbers")
        return
    largestNumber = numbers[0]
    for i in numbers:
        if(i > largestNumber):
            largestNumber = i

    print("Largest number is : ",largestNumber)


numSet = {1,4,6,2,12,5}
findLargest(*numSet)
findLargest()
findLargest(3,4,5)       