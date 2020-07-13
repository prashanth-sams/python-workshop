from datetime import datetime


def add_numbers(x, y):
    return x + y


def subtract_numbers(x, y):
    return x - y


def multiply_numbers(x, y):
    return x * y


def calculation(func):
    print(func(5, 5))


calculation(add_numbers)