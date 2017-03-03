import csv
f = open('eggs.csv')
csv_f = csv.reader(f)
myList = []
for row in csv_f:
    #print (row[2])
    myList.append(row[2])

print (myList)
