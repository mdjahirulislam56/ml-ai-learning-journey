import numpy as np

def make_diagonal(x):
    x = np.array(x)
    diag =  np.diag(x)
    return diag

diag_mat = make_diagonal([1,2,3])
print(diag_mat)