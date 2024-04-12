import math

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def power(x, y):
    return x ** y
def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None
def absolute_value(x):
    return abs(x)
def floor_division(x,y):
    return x // y
def modulus(x, y):
    return x % y

import random

def generate_random_number(start, end):
    return random.randint(start, end)
