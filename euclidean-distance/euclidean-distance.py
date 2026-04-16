import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    sum = 0
    if len(x) != len(y):
        raise ValueError
    for i in range(len(x)):
        sum += (x[i] - y[i])**2
    return np.sqrt(sum)
    