import numpy as np

probabilities = [0.5, 0.3, 0.2]
counts = np.random.multinomial(200, probabilities)

print("Product 1:", counts[0])
print("Product 2:", counts[1])
print("Product 3:", counts[2])
print("Total respondents:", counts.sum())
