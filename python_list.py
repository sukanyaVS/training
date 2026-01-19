#Write a Python Program to Count and Filter Odd and Even Numbers of Given List Using Loops

def my_function(numbers):
    for i in numbers:
        count_odd= 0
        count_even = 0
        even_numbers = []
        odd_numbers = []
    
    for i in numbers:
        if(i%2 == 0):
            count_even += 1
            even_numbers.append(i)
        else:
            count_odd += 1
            odd_numbers.append(i)

    print("Original list:",number_list)
    print("Count of even numbers : ", count_even , end="  and ")
    print("Count of odd numbers : ", count_odd)
    print("Even:",even_numbers)
    print("Odd:",odd_numbers)



number_list = [1,2,3,4,6,9,10,15,24,55,12]
my_function(number_list)