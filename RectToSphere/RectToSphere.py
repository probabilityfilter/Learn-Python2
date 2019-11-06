import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting toolkit

# Generate random floating point values
xMin = 0
xMax = 24
yMin = -90
yMax = 90
N = 100

xValues = np.random.rand(N)
yValues = np.random.rand(N)
xScaledValues = xMin + (xValues * (xMax - xMin))
yScaledValues = yMin + (yValues * (yMax - yMin))

# Plot x-y values in Cartesian co-ordinates
""" plt.scatter(xScaledValues, yScaledValues)
plt.title("Random Data")
plt.xlabel("x")
plt.ylabel("y")
plt.show() """

# Compute spherical co-ordinates
k = 1  # Arbitrary radius
# Initialize arrays
ra = np.linspace(0, 1, N, dtype=float)  # RA: Right Ascension
dec = np.linspace(0, 1, N, dtype=float)  # Dec: Declination
t = np.linspace(0, 1, N, dtype=float)
x3d = np.linspace(0, 1, N, dtype=float)
y3d = np.linspace(0, 1, N, dtype=float)
z3d = np.linspace(0, 1, N, dtype=float)

ra = np.multiply(xScaledValues, 2 * np.pi / 24)  # Convert RA's HH:MM:SS to Radians
dec = np.multiply(yScaledValues, 2 * np.pi / 360)  # Convert Dec's degrees to Radians

# Calculate projections of vector on x,y,z axis
t = np.multiply(k, np.cos(dec))  # Projection of unit vector k on x-y plane
x3d = np.multiply(t, np.cos(ra))  # Projection of t on x-axis
y3d = np.multiply(k, np.sin(dec))  # Projection of unit vector k on y-axis
z3d = np.multiply(t, np.sin(ra))  # Projection of t on z-axis

# Rotate all data points by 90 Deg to get the correct orientation
# Initialize new variables
x3dd = np.linspace(0, 1, N, dtype=float)
y3dd = np.linspace(0, 1, N, dtype=float)
z3dd = np.linspace(0, 1, N, dtype=float)

# 3D vector rotation
for i in range(0, N):
    tempx = x3d[i]
    tempy = y3d[i]
    tempz = z3d[i]
    x3dd[i] = tempx
    y3dd[i] = -tempz
    z3dd[i] = tempy

# Wireframe of Sky (sphere)
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection="3d")
# Wireframe of Sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
# Overlaying Wireframe of Sky over Candidate data
ax.plot_wireframe(x, y, z, rstride=10, cstride=10, color="b", alpha=0.1)

# Plot distribution of Candidates in the sky
ax.scatter(x3dd, y3dd, z3dd)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis")
ax.view_init(20, 45)
plt.axis("off")  # Remove axes for visual appeal
plt.show()
