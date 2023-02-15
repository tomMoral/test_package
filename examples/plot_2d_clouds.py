"""
Plot 2D clouds
==============
"""
import numpy as np
import matplotlib.pyplot as plt
from linear_regression import least_squares


# Generate data
n = 100
x = np.linspace(0, 1, n)

y = 2.5 * x + 0.1 * np.random.randn(n)
X = x[:, None]
predicted_coef = least_squares(X, y)
y_predicted = predicted_coef * x

plt.figure()
plt.scatter(x, y, c='k', label='data')
plt.plot(x, y_predicted, c='r', label='prediction')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()