Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
students={"Divakar":93,"Kishore":91,"Dhanush":90}
top_students=max(students,key=students.get)
print(top_students)
Divakar
print(students[top_students])
93
