import numpy as np

arr = np.random.randint(1, 101, size=(5, 5))
filename = "random_array.csv"

np.savetxt(filename, arr, delimiter=",", fmt="%d")
loaded = np.loadtxt(filename, delimiter=",", dtype=int)

print("Original array:")
print(arr)
print("Loaded array:")
print(loaded)
print("Arrays match:", np.array_equal(arr, loaded))
