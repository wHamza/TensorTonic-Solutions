import numpy as np

def cross_entropy_loss(y_true, y_pred):
    n = len(y_true)
    loss = 0
    
    
    for i in range(n):
        true_class = y_true[i]
        predicted_class = y_pred[i][true_class]
        loss += np.log(predicted_class)
    return (-1/n * loss)

    