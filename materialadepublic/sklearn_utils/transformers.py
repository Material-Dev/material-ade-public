import numpy as np
import pandas as pd

def StringTransformer(x):

    # print(type(x))
    x_shape = x.shape
    # print(x_shape)
    s = []
    for i in range(x_shape[0]):
        q = []
        for j in range(x_shape[1]):
            q.append(str(x[i,j]))
        s.append(q)

    return np.array(s)

def StringTransformer2(X):
    return pd.DataFrame(X).astype('float64').astype(str)