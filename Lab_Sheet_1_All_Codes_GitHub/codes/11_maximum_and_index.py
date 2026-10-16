import numpy as np

arr = np.random.randint(1, 101, size=10)
max_index = np.argmax(arr)

print("Array:", arr)
print("Maximum value:", arr[max_index])
print("Index position:", max_index)
