import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([12, 18, 33, 39, 55])

correlation_matrix = np.corrcoef(a, b)
correlation = correlation_matrix[0, 1]

print("Correlation matrix:")
print(correlation_matrix)
print("Correlation coefficient:", correlation)
