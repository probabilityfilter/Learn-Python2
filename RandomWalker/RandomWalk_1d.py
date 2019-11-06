# Random Walk in 1 dimension

import numpy as np
import matplotlib.pyplot as plt


def random_walk_1d(n):
    # Random choice of either left/right
    steps = np.random.choice([-1, +1], n)  # randomly select either left or right
    return np.cumsum(steps)


plt.subplot(2,2,1)
plt.plot(random_walk_1d(100))
plt.title('100 steps')
plt.xticks([])

plt.subplot(2,2,2)
plt.plot(random_walk_1d(1000))
plt.title('1000 steps')
plt.xticks([])

plt.subplot(2,2,3)
plt.plot(random_walk_1d(100000))
plt.title('100,000 steps')
plt.xticks([])

plt.subplot(2,2,4)
plt.plot(random_walk_1d(10000000))
plt.title('10,000,000 steps')
plt.xticks([])

plt.tight_layout()
plt.suptitle('Random Walk in 1D')
plt.show()