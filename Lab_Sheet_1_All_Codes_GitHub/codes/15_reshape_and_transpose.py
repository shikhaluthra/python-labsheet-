import numpy as np

arr = np.arange(1, 17)
matrix = arr.reshape(4, 4)
column_major_equivalent = np.transpose(matrix)

print("4x4 matrix:")
print(matrix)
print("After transpose:")
print(column_major_equivalent)
