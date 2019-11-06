# Random Walk in 2 dimensions

import numpy as np
import matplotlib.pyplot as plt


def random_walk_1d(n):
    # Random choice of either +1 or -1 (go left or right)
    steps = np.random.choice([-1, +1], (n, 50))  # Each of the 50 columns is a Walker
    return np.cumsum(steps, axis=0)


plt.plot(random_walk_1d(100000), lw=0.1)  # Plots 50 different lines (Walkers) on one plot
plt.title('100,000 steps')  # subplot title
plt.xticks([])

plt.tight_layout()
plt.suptitle('Multiple Random Walkers in 1D')  # main plot title
plt.show()