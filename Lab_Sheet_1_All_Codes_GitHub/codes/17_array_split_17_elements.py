import numpy as np

arr = np.arange(1, 18)
parts = np.array_split(arr, 4)

print("Original array:", arr)

for i, part in enumerate(parts, start=1):
    print(f"Part {i}: {part}, Size: {part.size}")
