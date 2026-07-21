Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def check even_odd(n):
    
SyntaxError: invalid syntax
def check_even_odd(n):
    if n%2==0:
        return"Even"
    else:
        return"Odd"

    
num=int(input("Enter your number:"))
Enter your number:93
result=check_even_odd(num)
print("The number is",result)
The number is Odd

num=int(input("Enter your number:"))
Enter your number:94
result=check_even_odd(num)
print("The number is",result)
The number is Even
