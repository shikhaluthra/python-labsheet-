import numpy as np

a = np.array([1, 2, 3])
b = np.array([[4, 5]])
c = np.array([6, 7, 8, 9])

a = a.reshape(1, -1)
b = b.reshape(1, -1)
c = c.reshape(1, -1)

result = np.concatenate((a, b, c), axis=1)

print("Result:", result)
