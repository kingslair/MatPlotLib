from tkinter import *

root = Tk()

height = 2
width = 3
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(root, text="Hello")
        b.grid(row=i, column=j)
        

mainloop()
