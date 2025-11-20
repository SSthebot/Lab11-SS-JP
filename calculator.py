import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Argument must be positive.")
    return math.log(b) / math.log(a)

def exp(a, b):
    return a ** b