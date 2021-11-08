import numpy as np


def linear_regression(X, y):
    return np.linalg.solve(np.dot(X.T, X), np.dot(X.T, y))


if __name__ == '__main__':
    n, p = 10, 3
    X = np.random.randn(n, p)
    true_coefs = np.random.randn(p)
    y = np.dot(X, true_coefs) + 0.01 * np.random.randn(n)
    pred_coefs = linear_regression(X, y)
    print(pred_coefs)
    print(true_coefs)