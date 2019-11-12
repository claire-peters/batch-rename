# This python script uses BeautifulSoup to batch rename .xml files based on information contained in the files.
# This script assumes that the .xmls being analyzed have similar formatting.

# I downloaded a host of .xmls with names consisting of random numbers. This script renames them according to the 
# contents of the files so I had an idea of who submitted the form and when it was submitted. This script reads
# .xmls in a given directory (including subdirectory) and replaces their names with ones based on specified strings
# in the .xml. You can alter other aspects of the new name as well - here, I replace spaces with underscores.

import os
import glob
import sys
import lxml.etree
from bs4 import BeautifulSoup as bs

fstart = DIRECTORYPATHHERE

folders = [x[0] for x in os.walk(fstart)]

for folder in folders:
    os.chdir(folder)

    files = glob.glob("*.xml")
    
    for file in files:
        data = open(file).read()
        soup = bs(data,'xml')
        clientName = soup.clientName.string
        reportYear = soup.reportYear.string
        reportType = soup.reportType.string
        newfilename = '-'.join([clientName, reportYear, reportType]) + ".xml"
        newfilename = newfilename.replace (' ', '_')
        os.rename(file, newfilename)
