import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

transpose = matrix.T
double_transpose = transpose.T

print("Original:")
print(matrix)
print("Transpose:")
print(transpose)
print("Transpose of transpose:")
print(double_transpose)
print("Equal to original:", np.array_equal(matrix, double_transpose))
