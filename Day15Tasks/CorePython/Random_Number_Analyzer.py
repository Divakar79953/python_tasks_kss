#Random Number Analyzer

import random


numbers = []

for i in range(10):
    numbers.append(random.randint(1, 50))


even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


unique_numbers = set(numbers)

print("Random Numbers:", numbers)
print("Even Count:", even_count)
print("Odd Count:", odd_count)
print("Unique Numbers:", unique_numbers)
