import numpy as np

arr = np.arange(1, 11)
print("Original:", arr)
print("Original dtype:", arr.dtype)

float_arr = arr.astype(float)
print("Float array:", float_arr)
print("New dtype:", float_arr.dtype)
