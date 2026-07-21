Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def list_sum(numbers):
    total=0
    for iin numbers:
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
def list_sum(numbers):
    total=0
    for i in numbers:
        total=total+i
        return total

numbers=[10,34,98,96,93,94]
result=list_sum(numbers)
print("Sum of elements=",result)
Sum of elements= 10
