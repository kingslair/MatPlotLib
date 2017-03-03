from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import time

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
op_array = np.array([])

def animate(i):
    pullData = open("bars_3d.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    zar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y,z = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
            zar.append(int(z))

    #print (xar)
    #print (yar)
    #print (zar)
    #for x1,y1,z1 in xar,yar,zar:
        #print (x1)
        #print (y1)
        #print (z1)
        #cs = [c] * len(xs)
        #cs[0] = 'c'
    ax.clear()
    ax.grid(zorder=0)
    #ax.bar(xar, yar,  zs=zar, zdir='y', color="blue", alpha=1)
    ax.scatter(xar, yar, zs=zar)

         
'''for c, z in zip(['r'], [10]):
    xs = np.arange(20)
    #xs =[1]
    ys = np.random.rand(20)
    #ys = [4]
    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    cs = [c] * len(xs)
    cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)
    #ax.bar(xs, ys, zs=z, zdir='z')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')'''

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
