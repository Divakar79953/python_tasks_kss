Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        return fact

    
num=int(input("Enter your numnber:"))
Enter your numnber:94
result=factorial(num)
print("Factiorial of ",num,"=",result)
Factiorial of  94 = 1

num=int(input("Enter your number:"))
Enter your number:93
result=factorial(num)
print("Factorial of",num,"=",result)
Factorial of 93 = 1
