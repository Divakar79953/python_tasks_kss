import numpy as np
import pandas as pd
import time

def read_numbers(filename):

    with open(filename, "r") as file:

        for line in file:

            try:
                yield float(line.strip())

            except ValueError:
                print("Invalid data:", line.strip())

def execution_time(func):

    def wrapper():

        start = time.time()

        result = func()

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper


@execution_time
def process_data():

    numbers = []

    for number in read_numbers("numbers.txt"):
        numbers.append(number)

    data = np.array(numbers)


    mean = np.mean(data)
    std = np.std(data)

    df = pd.DataFrame({
        "Mean": [mean],
        "Standard Deviation": [std]
    })

    print("NumPy Data:")
    print(data)

    print("\nResults:")
    print(df)


process_data()
