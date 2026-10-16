import numpy as np

a = np.array([10, 21, 32, 43, 54])
b = np.array([3, 4, 5, 6, 7])

remainder = np.mod(a, b)

print("Array 1:", a)
print("Array 2:", b)
print("Element-wise remainder:", remainder)
