import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.arctan(x)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')


ax.plot(x, y1, zs=5, zdir='y', label='Sine Wave')


ax.plot(x, y2, zs=-5, zdir='y', label='Cosine Wave')

ax.plot(x, y3, zs=5, zdir='x', label='Tangent Wave')


ax.plot(x, y4, zs=-5, zdir='x', label='Arctangent Wave')

ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

ax.legend()
plt.show()
