Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=int(input("Enter your number:"))
Enter your number:7
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
    if num>1 and is_prime:
        print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

        
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
