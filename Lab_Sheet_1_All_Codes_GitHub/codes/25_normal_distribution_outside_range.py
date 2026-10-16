import numpy as np

samples = np.random.normal(loc=0, scale=2, size=2000)
outside = samples[(samples < -4) | (samples > 4)]

print("Total samples:", len(samples))
print("Values outside [-4, 4]:", len(outside))
