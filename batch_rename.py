import os,glob,sys,lxml.etree
from bs4 import BeautifulSoup as bs

fstart = FOLDERPATHHERE

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
