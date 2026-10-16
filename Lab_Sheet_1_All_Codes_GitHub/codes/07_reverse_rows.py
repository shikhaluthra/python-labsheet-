import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
reversed_rows = arr[::-1]

print("Original:")
print(arr)
print("Rows reversed:")
print(reversed_rows)
