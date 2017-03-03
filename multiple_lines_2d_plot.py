import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)

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
    pullData1 = open("sampleText1.txt","r").read()
    dataArray1 = pullData1.split('\n')
    xar1 = []
    yar1 = []
    for eachLine1 in dataArray1:
        if len(eachLine1)>1:
            x,y = eachLine1.split(',')
            xar1.append(int(x))
            yar1.append(int(y))
    ax1.clear()
    ax2.clear()
    #Plot a Line Graph
    ax1.plot(xar,yar)
    ax2.plot(xar1,yar1)
    #Plot a Bar Graph
    #ax1.bar(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
