import sqlite3
import tkinter

class createGUIClass:
    def __init__(self,master):
        master.minsize(width=800, height=500)
        master.maxsize(width=1000, height=700)

root = tkinter.Tk()
createGUI = createGUIClass(root)

conn = sqlite3.connect('test.db')

myList = []
myList1 = []
myList2 = []
myList3 = []

cursor = conn.execute("SELECT id from COMPANY")
for row in cursor:
   myList.append(row)

cursor = conn.execute("SELECT name from COMPANY")
for row in cursor:
   myList1.append(row)

cursor = conn.execute("SELECT address from COMPANY")
for row in cursor:
   myList2.append(row)

cursor = conn.execute("SELECT salary from COMPANY")
for row in cursor:
   myList3.append(row)

conn.close()

for r in range(4):
    tkinter.Label(root, text='%s %s %s %s'%(str(myList[r]), str(myList1[r]), str(myList2[r]), str(myList3[r])),borderwidth=10).grid(row=r,column=0)
root.mainloop()
