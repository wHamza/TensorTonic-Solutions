import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    ust = (np.dot(a, b))
    # Write code here
    alt = (np.linalg.norm(a)*np.linalg.norm(b))
    if alt == 0:
        return 0
    else:
        return ust/alt