import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

    a = np.array(a)
    shape = a.shape
    if shape[0]*shape[1] != new_shape[0]*new_shape[1]:
        return []

    if a.shape != (new_shape[0],new_shape[1]):
        reshaped_matrix = a.reshape(new_shape).tolist()
    else:
        reshaped_matrix = a.tolist()
    
    return reshaped_matrix


mat = reshape_matrix(a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2))

print(mat)
