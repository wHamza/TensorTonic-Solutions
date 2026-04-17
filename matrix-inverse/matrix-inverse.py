import numpy as np

def matrix_inverse(A):
    A = np.asarray(A)
    det = np.linalg.det(A)
    if det == 0:
        return None
    else:
        return np.linalg.inv(A)