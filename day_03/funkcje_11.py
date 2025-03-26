import numpy as np
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time  =time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result
    return wrapper


@measure_time
def my_wait():
    time.sleep(3)

@measure_time
def my_for_sum():
    suma = 0
    for i in range(1,15000000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_sum_sum():
    total = sum(range(1,15000000))
    print("Sum is:", total)


def sum_np():
    total = np.sum(np.arange(1,15000000))
    print("Sum is:", total)

my_wait()

my_for_sum()

my_sum_sum()

sum_np()