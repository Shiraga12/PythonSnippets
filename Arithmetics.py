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
def maximum(x,y):
    return max(x,y)
def minimum(x,y):
    return min(x,y)
def logarithm(x,base):
    return math.log(x, base)
def factorial(x):
    return math.factorial(x)
def floor_division(x,y):
    return x // y
def modulus(x, y):
    return x % y
def round_number(x):
    return round(x)

import random

def generate_random_number(start, end):
    return random.randint(start, end)
