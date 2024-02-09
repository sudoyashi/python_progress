# Open all the documents and check to see if the document has a title, if so, remove it.
# Open all the documents and change the Author
import os
import fnmatch
from docx import Document

# Select all the docx
cwd = os.getcwd()
for dirpath, dirs, files in os.walk(cwd):
    for filename in fnmatch.filter(files, '*.docx'):
        # print (os.path.join(dirpath, filename))
        editFile = (os.path.join(dirpath, filename))
        document = Document(editFile)
        core_properties = document.core_properties
        # If the author filed is not ****, fill with **** email
        if (core_properties.author != 'joshua...email'):
            core_properties.author = 'joshua...newEmail'
        # Check if title is not empty, make it empty
        if (core_properties.title != ''):
            core_properties.title = ''
        # Save the file with the original name
        document.save(editFile)
        print ('Saved ', editFile)

 