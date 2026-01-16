def fingGrade(**marks):
    if(len(marks) == 0):
        print("There is no data")
        return
    print("Subjects and marks : ", marks)
    total_marks = 0

    for i in marks:
        total_marks += marks[i]

    print("Total Marks : ", total_marks)
    match total_marks:
        case A if total_marks >= 90 :
            print("Your grade is A")
        case B if 74 < total_marks < 90 :
            print("Your grade is B")
        case C if 50 <= total_marks < 75:
            print("Your grade is C")
        case _:
            print("You are failed")    
        



    

studA = {"X" : 30, "Y" : 20 , "Z" : 40}
studB = {"X" : 35, "Y" : 20 , "Z" : 20}

fingGrade()
fingGrade(**studA)
fingGrade(**studB)