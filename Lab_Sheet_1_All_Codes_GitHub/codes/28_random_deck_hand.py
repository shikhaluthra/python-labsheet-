import numpy as np

deck = np.arange(1, 53)
shuffled_deck = np.random.permutation(deck)
hand = shuffled_deck[:5]

print("Shuffled deck:")
print(shuffled_deck)
print("5-card hand:", hand)
