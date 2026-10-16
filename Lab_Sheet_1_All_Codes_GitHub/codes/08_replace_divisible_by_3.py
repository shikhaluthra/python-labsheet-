import numpy as np

arr = np.arange(1, 21)
arr[arr % 3 == 0] = -1

print("Result:", arr)
