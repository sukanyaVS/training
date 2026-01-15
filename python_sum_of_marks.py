sub1,sub2,sub3 = input("Enter marks of Malayalam, English and Maths : ").split()

sub1 = float(sub1)
sub2 = float(sub2)
sub3 = float(sub3)


print("Mark of Malayalam is :", sub1)
print("Mark of English is :", sub2)
print("Mark of Maths is :", sub3)

sumOfMarks = sub1 + sub2 + sub3
avgOfMarks = sumOfMarks/3

print(f"Sum of three subjects is : {sumOfMarks:.2f}") #Displayed with two decimal values
print(f"Average of three subjects is : {avgOfMarks:.2f}") #Displayed with two decimal values
