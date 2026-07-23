Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

n=int(input("Enter your number:"))
Enter your number:7
print("Factorial:",factorial(num))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("Factorial:",factorial(num))
NameError: name 'num' is not defined. Did you mean: 'sum'?
print("Factorial:",factorial(n))
Factorial: 5040
