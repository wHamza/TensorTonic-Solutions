import numpy as np

def softmax(x):
    a = 0
    if np.asarray(x).ndim == 1:
        a=0
    if np.asarray(x).ndim == 2:
        a=1
    
    
    shift_x = x- np.max(x, axis = a, keepdims = True)
    exps = np.exp(shift_x)
    return exps/np.sum(exps, axis = a, keepdims = True)