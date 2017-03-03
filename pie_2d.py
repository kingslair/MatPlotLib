import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'ATTACHED UE', 'DETACHED UE', 'UE WITH DATA', 'UE WITHOUT UE'
#sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()


def animate(i):
    pullData = open("pie_data.txt","r").read()
    dataArray = pullData.split('\n')
    sizes = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            sizes.append(int(eachLine))
    ax1.clear()
    #ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.pie(sizes, autopct='%1.1f%%',labels=labels,shadow=True, startangle=90)
    ax1.axis('equal')

ani = animation.FuncAnimation(fig1, animate, interval=1000)
plt.show()

