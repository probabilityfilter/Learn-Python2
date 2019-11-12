# Random Walk in 2 dimensions

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


def random_walk_1d(n):
    # Random choice of either +1 or -1 (go left or right)
    steps = np.random.choice([-1, +1], (n, 10000))  # Each of the 50 columns is a Walker
    return np.cumsum(steps, axis=0)


walkers = random_walk_1d(1000)
destination = walkers[:, :][-1, :]

# plt.subplot(1,2,1)
f, axes = plt.subplots(1, 2, sharex="col", sharey="row", figsize=(15, 6))
axes[0].plot(walkers, lw=0.1)  # Plots different lines (Walkers) on one plot

# plt.subplot(1,2,2)
y, x, _ = axes[1].hist(
    destination, bins=500, facecolor="green", alpha=0.75, orientation="horizontal"
)
axes[1].plot(np.arange(int(y.max())), np.zeros(int(y.max()), dtype=int), "k--")

plt.tight_layout()
plt.suptitle(
    "Left: 10,000 Random Walkers taking 1000 steps in 1D.  Right: Histogram of destination"
)  # main plot title
plt.show()
