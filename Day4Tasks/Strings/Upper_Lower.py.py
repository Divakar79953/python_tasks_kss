Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=input("Enter a string:")
Enter a string:Divakar
print("Upper case",s.upper())
Upper case DIVAKAR
print("lower case",s,lower())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print("lower case",s,lower())
NameError: name 'lower' is not defined
print("Lower case",s.lower())
Lower case divakar
