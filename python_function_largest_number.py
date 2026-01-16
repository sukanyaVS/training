def findLargest(*numbers):
    largestNumber = numbers[0]
    for i in numbers:
        if(i > largestNumber):
            largestNumber = i

    print("Largest number is : ",largestNumber)


numSet = {1,4,6,2,12,5}
findLargest(*numSet)            