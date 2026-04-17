import numpy as np

def dot_product(x, y):
    sum = 0
    if len(x) == len(y):
        for i in range(len(x)):
            sum += x[i] * y[i]
        return sum
    else:
        raise ValueError
    