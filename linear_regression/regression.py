import numpy as np


def least_squares(X, y):
    """
    Perform least squares regression.
    Finds coefficients w such that Xw ~= y

    Parameters
    ----------
    X : np.array, shape (n_samples, n_features)
        The input data
    y : np.array, shape (n_samples)
        The input targets

    Returns
    -------
    w : np.array, shape (n_features)
        The predicted regression coefficients
    """
    n, p = X.shape
    response = np.dot(X.T, y)  # Build response
    return np.linalg.solve(np.dot(X.T, X), response)


if __name__ == '__main__':
    n, p = 10, 3
    X = np.random.randn(n, p)
    true_coefs = np.random.randn(p)
    y = np.dot(X, true_coefs) + 0.01 * np.random.randn(n)
    pred_coefs = least_squares(X, y)
    print(pred_coefs)
    print(true_coefs)
