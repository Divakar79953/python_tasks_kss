Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

num=int(input("Enter the number of terms:"))
Enter the number of terms:7
fori in range(num):
    
SyntaxError: invalid syntax
for i in range(num):
    print(fibonacci(i),end=" ")

    
0 1 1 2 3 5 8 
