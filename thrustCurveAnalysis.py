###################################################
#                                                 #
#   Thrust Curve Finder                           #
#                                                 #
#                                                 #
###################################################

import requests
import urllib
import PyPDF2
import numpy as np
from os.path import exists
import matplotlib.pyplot as plt

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

indexCt=0
for i in dataPts:
    dataPts[indexCt]=i.split()
    indexCt+=1

for i in dataPts:
    indexCt=0
    for element in i:
        if element == ' ':
            del dataPts[indexCt]
        indexCt+=1

#print (dataPts)

xVals=[]
yVals=[]

for i in dataPts:
    xVals.append(float(i[0]))
    yVals.append(float(i[1]))

#print(xVals)
#print(yVals)

plt.plot(xVals,yVals)
plt.xlabel('Time (s)')
plt.ylabel('Thrust (N)')
plt.show()

