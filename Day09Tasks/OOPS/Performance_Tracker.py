# Performance Tracker (Decorators)

import time

def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()
        print("Execution Time:", end - start, "seconds")

    return wrapper


@timer
def task():
    print("Program is Running...")
    time.sleep(2)


task()
