import tkinter
import csv
f = open('class.csv')
csv_f = csv.reader(f)
myList = []
myList1 = []
myList2 = []
myList3 = []
for row in csv_f:
    #print (row[2])
    #myList.append(row[2])
    myList.append(row)
    myList1.append(row[0])
    myList2.append(row[1])
    myList3.append(row[2])

#print (myList)
class createGUIClass:
    def __init__(self,master):
        master.minsize(width=800, height=500)
        master.maxsize(width=1000, height=700)

root = tkinter.Tk()
createGUI = createGUIClass(root)
for r in range(5):
    tkinter.Label(root, text='%s'%(myList1[1]),
            borderwidth=10 ).grid(row=r,column=1)
    for c in range(len(myList)):
        tkinter.Label(root, text='%s'%(myList1[r]),
            borderwidth=10 ).grid(row=r,column=c)
root.mainloop(  )
