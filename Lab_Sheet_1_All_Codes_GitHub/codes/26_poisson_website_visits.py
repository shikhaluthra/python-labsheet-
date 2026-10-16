import numpy as np

visits = np.random.poisson(lam=5, size=60)
highest_minute = np.argmax(visits) + 1

print("Visits per minute:")
print(visits)
print("Minute with highest visits:", highest_minute)
print("Highest number of visits:", visits[highest_minute - 1])
