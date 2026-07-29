Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=int(input("Enter a number:"))
Enter a number:93
temp=num
sum=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
        sum=sum+fact
        temp=temp//10
    if sum==num:
        print(num,"is a Strong Number")
    else:
        print(num,"is not a Strong Number")

        
93 is not a Strong Number




