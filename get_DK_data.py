from bs4 import BeautifulSoup
import urllib
import sqlite3
import csv

conn = sqlite3.connect('golfbigboardTEST.db')
conn.text_factory = str
c = conn.cursor()

with open('DKSalaries.csv', 'rb') as f:
    reader = csv.reader(f)
    dk_data = list(reader)

del dk_data[0]

for i in dk_data:
    del i[0]
    del i[2]
    del i[3]

def createDkTable():
    c.execute('DROP TABLE IF EXISTS dkgolfer')
    c.execute('CREATE TABLE IF NOT EXISTS dkgolfer (full_name TEXT, salary INTEGER, scoring_avg FLOAT)')

def addGolfer(full_name,salary,scoring_avg):
    c.execute('INSERT INTO dkgolfer (full_name,salary,scoring_avg) VALUES (?,?,?)',(full_name,salary,scoring_avg))

createDkTable()

for k in dk_data:
    addGolfer(k[0],k[1],k[2])

# below is to get the price_array for the algorithm
price_array = []
full_name_array = []

for i in range(0,len(dk_data)):
    price_array.append(int(dk_data[i][1]))

for i in range(0,len(dk_data)):
    full_name_array.append(str(dk_data[i][0]))

print price_array
print full_name_array
#SELECT dkgolfer.full_name, salary, scoring_avg FROM dkgolfer INNER JOIN golfstratgolfer ON dkgolfer.full_name = golfstratgolfer.full_name

conn.commit()