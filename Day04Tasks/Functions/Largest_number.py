Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and  b>=c:
        return b
else:
    
SyntaxError: invalid syntax
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and  b>=c:
        return b
    else:
        return c

    
num1=int(input("Enter your first number:"))
Enter your first number:93
num2=int(input("Enter your second number:"))
Enter your second number:67
num3=int(input("Enter your third number:"))
Enter your third number:56
result=largest(num1,num2,num3)
print("Largest number=",result)
Largest number= 93
