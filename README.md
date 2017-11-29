# Batch Rename
This is a python script that allows for the batch renaming of .xml files based on information contained in the files. 

This script works under the assumption that the .xmls used have similar formatting - it works well for legal forms of the same type, for example. You'll need to install BeautifulSoup for this to work.

I downloaded a host of .xmls which had no descriptive names - just random numbers. I wanted to rename them according to the contents of the files so I had an idea of who submitted the form and when it was submitted. This script uses BeautifulSoup to analyze the contents of .xmls located in a given folder (including subfolders in said folder) and form a new file name based on specified strings in the .xml. It then replaces the old name with the new name generated. You can alter other aspects of the new name as well - here, I replaced spaces in a name with underscores (e.g. "Alice Smith" becomes "Alice_Smith").
