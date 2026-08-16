Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def  sum_digits(n):
    if n==0:
        return 0
    return(n%10)+sum_digits(n//10)

num=int(input("Enter your number:"))
Enter your number:93
print("Sum of digits:",sum_digits(num))
Sum of digits: 12
