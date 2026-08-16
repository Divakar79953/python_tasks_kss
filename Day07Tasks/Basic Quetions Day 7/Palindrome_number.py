Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num=int(input("Enter your number:"))
Enter your number:111
temp=num
reverse=0
while temp>0:
    digit=temp%10
    reverse=reverse*10
    temp=temp//10
    if reverse==num:
        print(num,"is a Palindrome Number")
    else:
        print(num,"is not a Palindrome Number")

        
111 is not a Palindrome Number
111 is not a Palindrome Number
111 is not a Palindrome Number


