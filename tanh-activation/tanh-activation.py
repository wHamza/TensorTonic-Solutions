import numpy as np

def tanh(x):
    inp = np.asarray(x)
    s= np.exp(inp)- np.exp(np.multiply(-1, inp))
    eksis = np.exp(inp)+ np.exp(np.multiply(-1, inp))

    return s/eksis