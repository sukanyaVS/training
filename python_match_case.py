mark = float(input("Enter the mark : "))

match mark:
    case A if mark >= 90 :
        print("Your grade is A")
    case B if 74 < mark < 90 :
        print("Your grade is B")
    case C if 50 <= mark < 75:
        print("Your grade is C")
    case _:
        print("You are failed")    
            