    ###################################################
    #                                                 #
    #   Thrust Curve Finder                           #
    #   (NAR Ripper and Excel Hell)                   #
    #                                                 #
    ###################################################
    
import requests
import matplotlib.pyplot as plt
from os.path import exists
import numpy as np
import PyPDF2
from openpyxl import load_workbook
import openpyxl
import re
import urllib
def main(engineType):
    
    
    wb = load_workbook("thrustCurveData.xlsx")
    sheet = wb["Sheet1"]
    headers = ['EndTime', 'Slope', 'Intercept']
    sheet.append(headers)
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:.]')
    
    choice = engineType
    
    if exists(choice + ".pdf"):
        print("File already exists")
    else:
        print("Downloading file...")
        try:
            urllib.request.urlretrieve(
                "https://www.nar.org/SandT/pdf/Estes/"+choice+".pdf", choice+".pdf")
        except urllib.error.HTTPError:
            print("File not found!")
            exit()
    pdfFileObj = open(choice+'.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numberOfPages = pdfReader.numPages
    pageObj = pdfReader.getPage(numberOfPages-1)
    pageText = pageObj.extractText(0)
    pageTextArr = pageText.split(choice)
    pdfFileObj.close()
    dataPts = []
    extractedData = []
    numbers = []
    datafound = False
    xVals = []
    yVals = []
    excelAdd = []
    temp = []
    
    pageTextArr = pageTextArr[2].split('\n')
    if len(pageTextArr) < 10:
    
        extractedData.append(pageTextArr[0].split(' '))
        for str in extractedData[0]:
            if str != '':
                numbers.append(str)
    
        for i in range(5):
            numbers.pop(0)
    
        if re.search('a-zA-Z', numbers[0]):
            print(' ')
        else:
            string = numbers[0]
            for i in string:
                if i.isalpha():
                    string = string.replace(i, '')
                    numbers[0] = string
    
        counter = 0
        symbolCt = 0
        longCt = 0
        for i in range(len(numbers)):
            if len(numbers[i]) > 7:
                longCt += 1
    
        for i in range(0, longCt+len(numbers)):
            for j in numbers[i]:
                if regex.search(j) != None:
                    symbolCt += 1
                if symbolCt > 1:
                    numbers.insert(i+1, numbers[i][(counter-1):])
                    numbers[i] = numbers[i][:(counter-1)]
                    break
                counter += 1
            symbolCt = 0
            counter = 0
    
        for i in range(0, len(numbers), 2):
            dataPts.append([float(numbers[i]), float(numbers[i+1])])
    
        for i in dataPts:
            xVals.append(float(i[0]))
            yVals.append(float(i[1]))
    
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
    else:
        pageTextArr.pop(0)
        pageTextArr.pop(-1)
        pageTextArr.pop(-1)
        pageTextArr.pop(-1)
        for i in range(len(pageTextArr)):
            extractedData.append(pageTextArr[i].split(' '))
        for i in range(len(extractedData)):
            for str in extractedData[i]:
                if str != '':
                    numbers.append(str)
        for i in range(0, len(numbers), 2):
            dataPts.append([float(numbers[i]), float(numbers[i+1])])
        for i in dataPts:
            xVals.append(float(i[0]))
            yVals.append(float(i[1]))
    
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
