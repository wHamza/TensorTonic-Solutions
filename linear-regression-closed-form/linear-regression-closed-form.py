import numpy as np

def linear_regression_closed_form(X, y):


    X, y = np.asarray(X), np.asarray(y)
    G = X.T @ X
    inv = np.linalg.pinv(G)
    W = inv @ X.T @ y
    
    return W