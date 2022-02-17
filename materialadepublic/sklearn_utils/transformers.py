import numpy as np

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