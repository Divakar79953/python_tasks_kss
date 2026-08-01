# Random Number Generator (Generators)
def numbers(n):
    for i in range(1,n+1):
        yield i

n=int(input("Enter the value of N:"))
for num in numbers(n):
    print(num)
