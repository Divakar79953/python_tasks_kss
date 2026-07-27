subjects=("Maths","Biology","Social")
students=set()
student_marks={}
def total_marks(marks):
    if len(marks)==0:
        return 0
    return marks[0]+total_marks(marks[1:])
def add_student():
    try:
        name = input("Enter student name:")
        marks = []

        for subject in subjects:
            mark = int(input(f"Enter marks for {subject}:"))
            marks.append(mark)

        students.add(name)
        student_marks[name] = marks
        print("Student added successfully.")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")

    except TypeError:
        print("Marks data type error.")


def display_students():
    if len(student_marks)==0:
       print("No student records.")

    else:
        for name,marks in student_marks.items():
          print(name,":",marks)

def calculate_average():
    try:
        name=input("Enter student name:")

        if name not in student_marks:
            raise NameError

        marks=student_marks[name]
        total=total_marks(marks)
        average=total/len(marks)

        print("Total marks:",total)
        print("Average Marks:",average)

    except NameError:
        print("Student name not found.")
    except ZeroDivisionError:
        print("Cannot didvide by zero.")
    except TypeError:
        print("Marks data type error.")

while True:
    print("\n1.Add Student")
    print("2.Display Students")
    print("3.Calculate Average")
    print("4.Exit")

    choice=input("Enter your choices:")

    if choice=="1":
        add_student()
    elif choice=="2":
        display_students()
    elif choice=="3":
        calculate_average()
    elif choice=="4":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
    

    
                
