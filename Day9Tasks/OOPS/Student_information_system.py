#Student Information System (Class & Object)

class student:
    def __init__(self,name,roll_number,marks,place):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
        self.place=place

    def display(self):
        print("Student Name:",self.name)
        print("Roll Number:",self.roll_number)
        print("Marks:",self.marks)
        print("Place:",self.place)

student1=student("Divakarnaidu",294,99,"TPG")
student2=student("Poojamadhuri",293,100,"TPG")
student3=student("Kishore",291,99,"NDD")
student4=student("Dhanush",290,98,"TPG")

student1.display()
student2.display()
student3.display()
student4.display()
