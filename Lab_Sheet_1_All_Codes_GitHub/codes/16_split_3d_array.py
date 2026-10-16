import numpy as np

arr = np.arange(32).reshape(2, 4, 4)
part1, part2 = np.split(arr, 2, axis=0)

print("Original shape:", arr.shape)
print("Part 1:")
print(part1)
print("Part 2:")
print(part2)
