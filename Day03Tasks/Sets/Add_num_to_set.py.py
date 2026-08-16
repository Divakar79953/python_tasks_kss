Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# write a programe to add an element to a set.
numbers={10,20,30,40,50}
numbers.add(93)
print(numbers)
{50, 20, 40, 10, 93, 30}



# Write a progarme to sub an element to a set.
numbers={12,34,56,67,89}
numbers.sub(67)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    numbers.sub(67)
AttributeError: 'set' object has no attribute 'sub'
numbers.sub(67)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    numbers.sub(67)
AttributeError: 'set' object has no attribute 'sub'

numbers={12,34,56,67,78}
numbers.remove(78)
print(numbers)
{34, 67, 56, 12}
