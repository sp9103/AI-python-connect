import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    return np.array(range(n*n), dtype=dtype).reshape((n, n))

def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        return np.zeros(shape, dtype=dtype)
    elif type == 1:
        return np.ones(shape, dtype=dtype)
    else:
        return np.empty(shape, dtype=dtype)

def change_shape_of_ndarray(X, n_row):
    new_col = int(X.size / n_row)
    return X.reshape((n_row, new_col))


def concat_ndarray(X_1, X_2, axis):
    try:
        result = np.concatenate((X_1, X_2), axis)
    except:
        return False
    return result


def normalize_ndarray(X, axis=99, dtype=np.float32):
    X = X.astype(dtype)
    if axis == 99:
        x_mean = np.mean(X)
        x_std = np.std(X)
    elif axis == 0:
        x_mean = np.mean(X, axis=0).reshape(1, -1)
        x_std = np.std(X, axis=0).reshape(1, -1)
    else:
        x_mean = np.mean(X, axis=1).reshape(-1, 1)
        x_std = np.std(X, axis=1).reshape(-1, 1)

    Z = (X - x_mean) / x_std
    return Z


def save_ndarray(X, filename="test.npy"):
    np.save(filename, X)


def boolean_index(X, condition):
    return X[eval(str("X") + condition)]


def find_nearest_value(X, target_value):
    return X[np.argmin(np.abs(X-target_value))]


def get_n_largest_values(X, n):
    # 확인 필요함
    return X[np.argsort(X[::-1])[:n]]
