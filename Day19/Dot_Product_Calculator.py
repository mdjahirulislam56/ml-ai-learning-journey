import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
    """
    Calculate the dot product of two vectors.
    Args:
    vec1 (numpy.ndarray): 1D array representing the first vector.
    vec2 (numpy.ndarray): 1D array representing the second vector.
    """
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    dot_prod = np.dot(vec1, vec2)
    
    return dot_prod

result = calculate_dot_product(vec1 = np.array([1, 2, 3]), vec2 = np.array([4, 5, 6]))
print(result)