#Write a program to add multiple student records into a file 
#Display 10th record then 15 th record using seek() and tell() method

def enter_stud_data():
    f = open('student-data.txt','w+')
    position = 0
    for i in range(10):
        name = input("Enter name of student : ")
        department = input("Enter department: ")
        print("-------------")
        f.write(f"Name : {name}  Department : {department}\n")
        position = i

    f.seek(0)
    print(f"Full records\n",f.read())

    #3rd and 8th record
    f.seek(0)
    lines = f.readlines()
    print(f"3rd record\n",lines[2])
    print(f"8th record\n",lines[7])
    


try:
 enter_stud_data()
except FileNotFoundError:
 print("Error: File not found.") 