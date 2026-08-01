# Infinite Even Number Generator (Generators)


def even_number():
    num=2

    while True:
        yield num
        num=num+2

n=int(input("Enter how many even numbers you want:"))
gen=even_number()
for i in range(n):
    print(next(gen))
