Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=input("Enter a string:")
Enter a string:Divakar Naidu
sub=input("Enter a substring to search:")
Enter a substring to search:Naidu
if sub in s:
    print("Substring exists in the string")
else:
    print("Substring does not exist in the string")

    
Substring exists in the string

sub=input("Enter a substring to search:")
Enter a substring to search:Vamisetti
if sub in s:
    print("subbstring exist in the string")
else:
    print("Substring does not exist in  the string")

    
Substring does not exist in  the string
