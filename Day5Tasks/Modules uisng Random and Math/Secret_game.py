Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
import math
secret=random.randint(1,50)
for i in range(5):
    guess=int(input("Enter your guess:"))
    if guess==secret:
        print("Congratulations! you guessed the correct number.")
        break

    
Enter your guess:7
Enter your guess:4
Enter your guess:
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    guess=int(input("Enter your guess:"))
ValueError: invalid literal for int() with base 10: ''

difference=math.fabs(screat-guess)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    difference=math.fabs(screat-guess)
NameError: name 'screat' is not defined. Did you mean: 'secret'?

# Guess Secret

import random
import math
secret=random.randint(1,50)
for i in range(5):
    guess=int(input("Enter your guess:"))
    if guess=secret:
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

# Guess&Secret

import random
import math
secret=random.randint(1,50):
    
SyntaxError: invalid syntax

 

import random
import math
secret=random.randint(1,50)
for i in range(5):
    guess=int(input("Enter your guess:"))
    if guess==secret:
        print("Congratulations you guessed the correct number.")
        break
    difference=math.fabs(secret-guess)
    print("You are",difference,"away from the correct number.")
else:
    print("Game over")
    print("Correct number=",secret)

    
Enter your guess:7
You are 38.0 away from the correct number.
Enter your guess:45
Congratulations you guessed the correct number.
