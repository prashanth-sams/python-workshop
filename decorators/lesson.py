from datetime import datetime


def calculation(func):
    def time_wrapper(x, y):
        start = datetime.now()
        print(func(x, y))
        end = datetime.now()
        return end - start
    return time_wrapper


@calculation
def add_numbers(x, y):
    return x + y


@calculation
def subtract_numbers(x, y):
    return x - y


@calculation
def multiply_numbers(x, y):
    return x * y


print(multiply_numbers(5, 5))
