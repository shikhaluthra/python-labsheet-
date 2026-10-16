import numpy as np

flips = np.random.binomial(n=1, p=0.7, size=200)
heads = np.sum(flips)
proportion = heads / 200

print("Number of heads:", heads)
print("Number of tails:", 200 - heads)
print("Observed proportion of heads:", proportion)
