# import packages
# This script finds all files that end with .xml and puts them into a list. In that list
# extract the xml value pairs, remove duplicates and write the pairs into sheet1 
# of a new Excel sheet within columns B:Z
# Finally, save the XML as an XLSX into the xlsx directory.

import xml.etree.ElementTree as ETree
import pandas as pd
import os
import pathlib
from os import listdir, path
from pathlib import Path

cwd = os.getcwd()
files = []
for file in listdir(cwd):
    if file.endswith('.xml'):
        files.append(path.join(cwd, file))

for xml in files:
    fileroot = Path(xml).stem
    tree = ETree.parse(xml)
    root = tree.getroot()
    valuePairs = []  # empty array assigned to A
    for elements in root:
        valuePair = {}  # empty array; store data values in key:value pair
        for element in list(elements):
            valuePair.update({element.tag: element.text})  # updating dictionary with(tag -> Columns, text -> Rowdata)
            valuePairs.append(valuePair)  # Append key:value pair to A list
        df = pd.DataFrame(valuePairs)  # Create dataframe (df)
        df.drop_duplicates(keep='first', inplace=True)  # Only keep first, ignore all others
        df.reset_index(drop=True, inplace=True)
        writer = pd.ExcelWriter(cwd + '\\' + 'xlsx' + '\\' + fileroot + '.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='sheet1')
        worksheet = writer.sheets['sheet1']
        worksheet.set_column('B:Z', 30)  # Set column char to 30 for columns from B to Z
        writer._save()
    print(df)
    print('XML file has been parsed. Open at ' + fileroot + '.xlsx...')