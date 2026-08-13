#Advanced Simulation System

import random
import numpy as np
import pandas as pd
import math



class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 50:
            return "C"

        else:
            return "Fail"


try:


    marks = [random.randint(0, 100) for i in range(5)]


    marks_array = np.array(marks)

    names = ["A", "B", "C", "D", "E"]

    students = []

    for name, mark in zip(names, marks_array):
        student = Student(name, mark)
        students.append(student)

    data = {
        "Name": names,
        "Marks": marks_array
    }

    df = pd.DataFrame(data)

    grades = []

    for student in students:
        grades.append(student.grade())

    df["Grade"] = grades

    average = math.fsum(marks_array) / len(marks_array)

    print("Exam Results:")
    print(df)

    print("\nAverage Marks:", average)

    with open("exam_report.txt", "w") as file:

        file.write("Exam Report\n")
        file.write("================\n")
        file.write(str(df))

        file.write("\n\nAverage Marks: ")
        file.write(str(average))

    print("\nReport saved successfully.")


except Exception as e:

    print("Error:", e)
