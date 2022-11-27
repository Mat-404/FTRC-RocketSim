###################################################
#                                                 #
#   Thrust Curve Finder                           #
#   (NAR Ripper and Excel Hell)                   #
#                                                 #
###################################################

def main(engineType):

    import requests
    import urllib
    import openpyxl
    from openpyxl import load_workbook
    import PyPDF2
    import numpy as np
    from os.path import exists
    import matplotlib.pyplot as plt

    wb = load_workbook("thrustCurveData.xlsx")
    sheet = wb["Sheet1"]
    headers = ['EndTime', 'Slope', 'Intercept']
    sheet.append(headers)

    choice = engineType

    if exists(choice + ".pdf"):
        print("File already exists")
    else:
        print("Downloading file...")
        urllib.request.urlretrieve("https://www.nar.org/SandT/pdf/Estes/"+choice+".pdf", choice+".pdf")

    pdfFileObj = open(choice+'.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numberOfPages = pdfReader.numPages
    pageObj = pdfReader.getPage(numberOfPages-1)
    pageText = pageObj.extractText(0)
    pageTextArr = pageText.split('\n')
    # print(pageText)
    dataPts = []
    datafound = False
    for i in pageTextArr:
        if datafound:
            dataPts.append(i)
        if i.find(choice) != -1:
            if i.find('Estes '+choice) != -1:
                datafound = False
            else:
                datafound = True

    pdfFileObj.close()
    dataPts.pop()
    dataPts.pop()
    dataPts.pop()

    indexCt = 0
    for i in dataPts:
        dataPts[indexCt] = i.split()
        indexCt += 1

    for i in dataPts:
        indexCt = 0
        for element in i:
            if element == ' ':
                del dataPts[indexCt]
            indexCt += 1

    xVals = []
    yVals = []
    inters = []

    for i in dataPts:
        xVals.append(float(i[0]))
        yVals.append(float(i[1]))

    xVals.pop(0)
    excelAdd = []
    temp = []
    for i in range(len(xVals)):
        temp.append(xVals[i])
        if i != 0:
            temp.append((yVals[i]-yVals[i-1])/(xVals[i]-xVals[i-1]))
        else:
            temp.append((yVals[i])/(xVals[i]))
        b = yVals[i] - temp[1]*xVals[i]
        temp.append(b)
        excelAdd.append(temp)
        temp = []

    # append data to excel sheet
    for value in excelAdd:
        sheet.append(value)


    wb.save("thrustCurveData.xlsx")

    return excelAdd