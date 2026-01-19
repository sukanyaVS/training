
students = [
  ("Anu", 78),
  ("Rahul", 45),
  ("Meera", 92),
  ("Kiran", 33),
  ("Arjun", 60),
  ("Anu", 78)
]

def grade_generator(data):
    for name,mark in data:
        
        match mark:
            case A if mark >= 90:
                grade = "A"
            case B if mark >= 75:
                grade = "B"
            case C if mark >= 50:
                grade = "C" 
            case _:
                grade = 'Fail'

        yield (name,mark,grade)  
    
    

def print_data(students):
    student_list = list(grade_generator(students))
    print("Result List:",student_list)

    student_dict = {}

    for name, marks, grade in student_list:
     student_dict[name] = grade

    print("Student dictionary:",student_dict)
print_data(students)