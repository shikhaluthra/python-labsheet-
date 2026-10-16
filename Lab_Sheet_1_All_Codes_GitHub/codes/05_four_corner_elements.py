import numpy as np

arr = np.arange(1, 37).reshape(6, 6)
corners = arr[[0, 0, -1, -1], [0, -1, 0, -1]]

print("Array:")
print(arr)
print("Four corners:", corners)
