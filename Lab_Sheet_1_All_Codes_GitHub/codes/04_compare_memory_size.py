import numpy as np
import sys

values = [1, 2, 3, 4, 5]
python_list = values
numpy_array = np.array(values)

print("Python list:", python_list)
print("NumPy array:", numpy_array)
print("Python list memory:", sys.getsizeof(python_list), "bytes")
print("NumPy array memory:", sys.getsizeof(numpy_array), "bytes")
