# Random Walk in 2 dimensions

import numpy as np
import matplotlib.pyplot as plt
# from scipy.stats import norm
import matplotlib.mlab as mlab

def random_walk_1d(n):
    # Random choice of either +1 or -1 (go left or right)
    steps = np.random.choice([-1, +1], (n, 10000))  # Each of the 50 columns is a Walker
    return np.cumsum(steps, axis=0)


walkers = random_walk_1d(1000)
print(walkers.shape)
# print(Walkers[:,0][-1])
# print(Walkers[:,1][-1])
destination = walkers[:,:][-1,:]
print(destination.shape)
# print(destination)

# plt.subplot(1,2,1)
f, axes = plt.subplots(1, 2, sharex='col', sharey='row', figsize=(15, 6))
#plt.title('100,000 steps')  # subplot title
axes[0].plot(walkers, lw=0.1)  # Plots 50 different lines (Walkers) on one plot

#axes[1].xticks([])

# plt.plot(walkers, lw=0.7, sharey='row')  # Plots 50 different lines (Walkers) on one plot
# plt.title('100,000 steps')  # subplot title
# plt.xticks([])

#plt.subplot(1,2,2)
#plt.hist(destination, bins=50, facecolor='green', alpha=0.75, orientation="horizontal")
y, x, _ = axes[1].hist(destination, bins=500, facecolor='green', alpha=0.75, orientation="horizontal")
axes[1].plot(np.arange(int(y.max())),np.zeros(int(y.max()), dtype=int), 'k--')
# y, x, _ = plt.hist(hdata)
print(x.max())
print(y.max())

plt.tight_layout()
plt.suptitle('Left: 10,000 Random Walkers taking 1000 steps in 1D.  Right: Histogram of destination')  # main plot title
plt.show()

