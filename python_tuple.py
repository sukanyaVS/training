#Create a tuple of even numbers from another tuple
def create_tuple(numbers):
    new_list = list(numbers)
    even_numbers = []
    for i in new_list:
        if(i%2 == 0):
            even_numbers.append(i)
    print("Original:",numbers)
    new_tuple = tuple((even_numbers))
    print("New tuple:",new_tuple)

numbers = (1,2,3,4,6,9,10,15,24,55,12)
create_tuple(numbers)


#Find sum of elements in a tuple

def calculate_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Number Tuple:",numbers)
    print("Sum:",sum)

numbers = (1,2,3,4,5)
calculate_sum(numbers)