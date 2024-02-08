# Creates a list of directories if they do not exist. This creates
# the CDs, software, and drivers directories, as indicated by directory.csv
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

with open('directory.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for column in row:
            print(column)
            p = pathName + '\\' + column
            Path(p).mkdir(parents=True, exist_ok=True)