import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
#theta = ([1,10], [0,0])
#theta = np.linspace(-1 * np.pi, 1 * np.pi, 100)
#z = np.linspace(-1, 1, 100)
z = np.linspace(1,10,num=2)
r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)
x = r * 2
y = r * 2
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
