Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
impor random
SyntaxError: invalid syntax. Perhaps you forgot a comma?
import random
import math
numbers=[]
for i in range(20):
    num=random.randint(1,200)
    numbers.append(num)

    
print("Random numbers=",numbers)
Random numbers= [21, 177, 172, 199, 23, 191, 54, 140, 122, 47, 173, 53, 153, 151, 168, 42, 183, 102, 79, 47]
maximum=max(numbers)
minimum=min(numbers)
print("Maximum=",maximum)
Maximum= 199
print("Minimum=",manimum)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("Minimum=",manimum)
NameError: name 'manimum' is not defined. Did you mean: 'maximum'?
print("Minimum=",minimum)
Minimum= 21
print("Square root of Maximum=",math.sqrt(maximum))
Square root of Maximum= 14.106735979665885
print("Logarithm of Minimum=",math.log(minimum))
Logarithm of Minimum= 3.044522437723423
