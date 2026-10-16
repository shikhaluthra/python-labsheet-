import numpy as np

matrix = np.random.randint(10, 51, size=(3, 3))
sorted_matrix = np.sort(matrix, axis=1)

print("Original matrix:")
print(matrix)
print("Rows sorted in ascending order:")
print(sorted_matrix)
