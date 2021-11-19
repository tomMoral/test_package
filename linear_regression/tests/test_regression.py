import numpy as np
from linear_regression import linear_regression


def test_dimensions():
    X = np.random.randn(3, 2)
    y = np.random.randn(3 )
    coefs = linear_regression(X, y)
    assert len(coefs) == 2

