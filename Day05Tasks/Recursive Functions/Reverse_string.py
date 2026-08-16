Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def reverse_string(s):
    if len(s)==0;
    
SyntaxError: invalid syntax
def reverse_string(s):
    if len(s)==0:
        return s
    return reverse_string(s[1:])+s[0]

text=input("Enter your text:")
Enter your text:Python at kss
print("Reverse string:",reverse_string(text))
Reverse string: ssk ta nohtyP
