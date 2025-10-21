import numpy as np

def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    a = np.array(a)
    b = np.array(b)
    # print(a.ndim, b.ndim, a.shape, b.shape)
    if (a.shape == b.shape):
        result = (a+b).tolist()
    else:
        return -1
    
    return result

r = vector_sum(a = [1, 3], b = [4,5])

print(r)