# Random Walk in 1 dimension, no class, no vectorization

import random

n = 100
x = 0
path = [x]
for i in range(n):
    x += 2 * random.randint(0, 1) - 1
    path.append(x)

print(path)
