import sqlite3
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import random


def update_db(op_array):
    conn = sqlite3.connect('test.db')
    random_number = random.randint(10, 180)
    query = conn.execute("UPDATE COMPANY SET salary = %s where ID = 1" % (random_number))
    random_number = random.randint(10, 180)
    query = conn.execute("UPDATE COMPANY SET salary = %s where ID = 2" % (random_number))
    random_number = random.randint(10, 180)
    query = conn.execute("UPDATE COMPANY SET salary = %s where ID = 3" % (random_number))
    random_number = random.randint(10, 180)
    query = conn.execute("UPDATE COMPANY SET salary = %s where ID = 4" % (random_number))

    cursor = conn.execute("SELECT salary from COMPANY")
    for row in cursor:
        op_array = np.append(op_array, row)
    print (op_array)
    return op_array
    conn.close()


myList = []
op_array = np.array([])

#query = conn.execute("UPDATE COMPANY SET salary = 30 where ID = 1")
#query = conn.execute("UPDATE COMPANY SET salary = 40 where ID = 2")
#query = conn.execute("UPDATE COMPANY SET salary = 10 where ID = 3")
#query = conn.execute("UPDATE COMPANY SET salary = 40 where ID = 4")

'''cursor = conn.execute("SELECT salary from COMPANY")
for row in cursor:
   myList.append(row)
   op_array = np.append(op_array, row)'''

op_array = update_db(op_array)
#print (myList)
#print (op_array)
#conn.close()

#start plotting
'''mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
#z = np.linspace(1,10,num=2)
z = op_array
r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)
x = r * 2
y = r * 2
ax.plot(x, y, z, label='parametric curve')
ax.legend()'''

while True:
    plt.show()
    plt.pause(0.05)
    op_array = update_db(op_array)
    #start plotting
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #z = np.linspace(1,10,num=2)
    z = op_array
    r = z**2 + 1
    #x = r * np.sin(theta)
    #y = r * np.cos(theta)
    x = r * 2
    y = r * 2
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()



