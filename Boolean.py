import math

def is_even(x):
    return x % 2 == 0
def is_odd(x):
    return x % 2 != 0
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
