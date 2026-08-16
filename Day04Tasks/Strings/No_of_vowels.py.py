Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=input("Enter a string:")
Enter a string:Divakar Naidu
count=0
vowels="aeiouAEIOU"
for ch in s:
    if ch in vowels:
        count+=1
        print("Number of vowels:",count)

        
Number of vowels: 1
Number of vowels: 2
Number of vowels: 3
Number of vowels: 4
Number of vowels: 5
Number of vowels: 6
