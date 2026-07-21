Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=12
b=34
c=24
print(a+b+c)/3
70
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a+b+c)/3
TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
a=12
b=45
c=34
average=(a+b+c)/3
print("Averagge=",average)
Averagge= 30.333333333333332
