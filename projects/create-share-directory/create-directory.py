import os
import csv
from pathlib import Path

# create the file directory.csv

with open('directory.csv', 'w') as directory:
    directory.write('CDs,software,drivers')

# setup variable that loads all *.csv information
    
pathName = os.getcwd()
directoryFiles = os.listdir(pathName)
csvFiles = []
for file in directoryFiles:
    if file.endswith(".csv"):
        csvFiles.append(file)

#for file in directoryFiles:
#    file = open(os.path.join(pathName)) # command broke because trying to read a directory as a file!

with open('directory.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for column in row:
            print(column)
            p = pathName + '\\' + column
            Path(p).mkdir(parents=True, exist_ok=True)