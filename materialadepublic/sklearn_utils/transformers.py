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
    X_transformed = pd.DataFrame()

    for column in X.columns:
        if np.issubdtype(X[column].dtype, np.number):
            X_transformed[column] = X[column].astype('float64').astype(str)
        else:
            X_transformed[column] = X[column].astype(str)

    return X_transformed