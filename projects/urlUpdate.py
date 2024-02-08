# Create a script that iterates through all .bat files in the directory, searches for the string 
# c:\program files\internet explorer\iexplore.exe and replaces it with 
# C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# This is CASE-SENSITIVE, so check to see if the text is different. C:\Program Files is different from c:\program files.

import os
from os import listdir, path
from pathlib import Path
import sys
import fileinput

# list all .bat files

cwd = os.getcwd()
files = []
for file in listdir(cwd):
    if file.endswith('.bat'):
        files.append(path.join(cwd, file))

# Declare search strings
        
textToSearch = "c:\program files\internet explorer\iexplore.exe"
textToReplace = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

for bat in files:
    with open(bat, 'r') as file:
        filedata = file.read()
        print("Read", bat)
    filedata = filedata.replace(textToSearch, textToReplace)
    with open(bat, 'w') as file:
        file.write(filedata)
        print("Write", bat)