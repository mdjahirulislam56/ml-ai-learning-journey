import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    matrix = np.array(matrix)
    result = matrix*scalar
    return result

result = scalar_multiply(matrix = [[1, 2], [3, 4]], scalar = 2)
print(result)