import numpy as np
def elu(x, alpha):
    for i in range(len(x)):
        if x[i] >0:
            pass
        else:
            x[i] = alpha * (np.exp(x[i])- 1)

    return x