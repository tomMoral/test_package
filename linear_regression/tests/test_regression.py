import numpy as np
import pytest
from numpy.testing import assert_almost_equal
from linear_regression import least_squares


@pytest.mark.parametrize("n", [2, 10, 20])
def test_dimensions(n):
    rng = np.random.RandomState(0)
    X = rng.randn(n, 3)
    y = rng.randn(n)
    coefs = least_squares(X, y)
    assert len(coefs) == 3


def test_minimum():

    rng = np.random.RandomState(0)
    X = rng.randn(3, 2)
    y = rng.randn(3)
    coefs = least_squares(X, y)
    gradient = np.dot(X.T, np.dot(X, coefs) - y)
    assert_almost_equal(gradient, 0)


def test_no_nan():
    rng = np.random.RandomState(42)
    X = rng.randn(3, 2)
    y = rng.randn(3)
    coefs = least_squares(X, y)
    assert not np.isnan(coefs).any()


def test_recovery():
    rng = np.random.RandomState(0)
    X = rng.randn(3, 2)
    true_coefs = rng.randn(2)
    y = np.dot(X, true_coefs)
    predicted_coefs = least_squares(X, y)
    assert_almost_equal(true_coefs, predicted_coefs)
