# Student Score Processor
import math
students=[
    ("D",94),
    ("I",93),
    ("V",78),
    ("A",65),
    ("K",79),
    ("A",57),
    ("R",89)
    ]
student_data=dict(students)
above_50=[]
for name,marks in student_data.items():
    if marks>50:
        above_50.append(name)

average=math.fsum(student_data.values())/len(student_data)
print("Student Data:",student_data)
print("Students Above 50:",above_50)
print("Average Marks:",average)

with open("Student_results.txt","w")as file:
    file.write("Student Data:\n")
    file.write(str(student_data))

    file.write("\nStudents Above 50:\n")
    file.write(str(above_50))

    file.write("\nAverage Marks:\n")
    file.write(str(average))
    
