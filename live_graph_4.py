import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
fig.suptitle('Line Graph', fontsize=14, fontweight='bold')
fig.patch.set_visible(False)
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("sampleText.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    #Plot a Line Graph
    ax1.plot(xar,yar)
    #Plot a Bar Graph
    #ax1.bar(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
