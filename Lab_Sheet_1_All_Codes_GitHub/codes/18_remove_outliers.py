import numpy as np

arr = np.array([10, 12, 11, 13, 12, 14, 100, 9, 11, 10], dtype=float)

mean = np.mean(arr)
std = np.std(arr)

lower = mean - 2 * std
upper = mean + 2 * std

filtered = arr[(arr >= lower) & (arr <= upper)]

print("Original array:", arr)
print("Mean:", mean)
print("Standard deviation:", std)
print("Valid range:", lower, "to", upper)
print("Array without outliers:", filtered)
