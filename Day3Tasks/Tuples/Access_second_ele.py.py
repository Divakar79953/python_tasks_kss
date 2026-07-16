Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=(12,34,56,78)
print(num[1])
34
print(num[4])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(num[4])
IndexError: tuple index out of range
print(num[3])
78
