import sqlite3
import numpy as np

global op_array
op_array = np.array([])
conn = sqlite3.connect('test.db')

query = conn.execute("UPDATE COMPANY SET salary = 60 where ID = 1")
query = conn.execute("UPDATE COMPANY SET salary = 40 where ID = 2")
query = conn.execute("UPDATE COMPANY SET salary = 10 where ID = 3")
query = conn.execute("UPDATE COMPANY SET salary = 40 where ID = 4")

cursor = conn.execute("SELECT salary from COMPANY")
for row in cursor:
   op_array = np.append(op_array, row)

conn.close()
