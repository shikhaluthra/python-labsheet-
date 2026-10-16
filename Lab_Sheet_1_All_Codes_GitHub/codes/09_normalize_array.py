import numpy as np

arr = np.array([10, 20, 30, 40, 50], dtype=float)
normalized = (arr - arr.min()) / (arr.max() - arr.min())

print("Original:", arr)
print("Normalized:", normalized)
