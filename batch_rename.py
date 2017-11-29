import os,glob,sys,lxml.etree
from bs4 import BeautifulSoup as bs

fstart = FOLDERPATHHERE

folders = [x[0] for x in os.walk(fstart)]

for folder in folders:
    os.chdir(folder)

    files = glob.glob("*.xml")
    print files
    
    for file in files:
        data = open(file).read()
        soup = bs(data,'xml')
        clientName = soup.clientName.string
        print clientName
        reportYear = soup.reportYear.string
        print reportYear
        reportType = soup.reportType.string
        print reportType
        newfilename = '-'.join([clientName, reportYear, reportType]) + ".xml"
        print newfilename
        newfilename = newfilename.replace (' ', '_')
        os.rename(file, newfilename)
