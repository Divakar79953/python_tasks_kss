Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def count_vowels(text):
    count=0
    for i in text:
        if i in "aeiouAEIOU":
            count=count+1
            return count

        
word=input("Enter a string:")
Enter a string:Divakar Naidu
result=count_vowels(word)
print("Number of vowels=",result)
Number of vowels= 1
