###################################################
#                                                 #
#   Thrust Curve Finder                           #
#                                                 #
#                                                 #
###################################################

import requests
import urllib
import PyPDF2
from os.path import exists

choice = input("What engine type: ")

if exists(choice + ".pdf"):
    print("File exists")
else:
    urllib.request.urlretrieve("https://www.nar.org/SandT/pdf/Estes/"+choice+".pdf", choice+".pdf")

pdfFileObj = open(choice+'.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numberOfPages=pdfReader.numPages
pageObj = pdfReader.getPage(numberOfPages-1)
pageText=pageObj.extractText(0)
pageTextArr=pageText.split('\n')
#print(pageText)
print ('\n')
dataPts = []
datafound=False
for i in pageTextArr:
    if datafound:
        dataPts.append(i)
    if i.find(choice) != -1:
        if i.find('Estes '+choice) !=-1:
            datafound=False
        else:
            datafound=True

pdfFileObj.close()
dataPts.pop()
dataPts.pop()
dataPts.pop()

#print(dataPts)

currentchar=''
prevchar=''
thrustCurve = []
for i in dataPts:
    for element in i:
        currentchar=element
        if currentchar == ' ' and prevchar == ' ':
            i.replace(' ','',1)
        prevchar=currentchar

    tempString=i.split(' ')
    print(tempString)
    thrustCurve.append(tempString[0])
    thrustCurve.append(tempString[1])
