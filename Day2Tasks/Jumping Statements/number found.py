Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
numbers=[10,20,30,40,50]
search=int(input("Enter the number to search:"))
Enter the number to search:30
for i in numbers:
    if i==search:
        print("Number found!")
        break

    
Number found!
