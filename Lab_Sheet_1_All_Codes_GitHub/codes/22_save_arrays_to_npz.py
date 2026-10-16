import numpy as np

a = np.array([1, 2, 3, 4])
b = np.arange(6).reshape(2, 3)
c = np.array([[10, 20], [30, 40], [50, 60]])

np.savez("three_arrays.npz", first=a, second=b, third=c)

data = np.load("three_arrays.npz")

print("Arrays stored in the NPZ file:")
print(data.files)

for name in data.files:
    print(f"{name}:")
    print(data[name])
