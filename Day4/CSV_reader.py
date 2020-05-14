import csv
fields=[]
rows=[]
filename="electronics.csv"
with open(filename,'r') as readCSV:
    csvReader=csv.reader(readCSV)
    fields=next(csvReader)
    for row in csvReader:
        rows.append(row)

print(fields)

for row in rows[:5]:
    print(row)
