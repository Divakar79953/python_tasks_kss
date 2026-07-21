Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=input("Enter a string:")
Enter a string: Divakar Naidu
result=""
for ch in s:
    if ch not in result:
        result=result+ch

        
print("String after removing duplicates:",result)
String after removing duplicates:  DivakrNdu
