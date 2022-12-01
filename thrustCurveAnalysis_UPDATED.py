    ###################################################
    #                                                 #
    #   Thrust Curve Interpereter                     #
    #                                                 #
    ###################################################
    
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import openpyxl
def main(engineType):



    DataWorkbook = load_workbook("EngineDataSheet.xlsx")
    EngineData = DataWorkbook[engineType]

    xValues = EngineData['A2':'A21']
    yValues = EngineData['B2':'B21']
        # get rate of change of thrust from excel sheet
    slopeValues = EngineData['D3':'D21']
    timeValues = EngineData['E3':'E21']

    outputValues = []
        # calculate intercepts and append to outputValues
    for i in range(0, len(slopeValues)):
        if i == 0:
            intercept = 0
            outputValues.append([timeValues[i][0].value, slopeValues[i][0].value, intercept])
        else:
            intercept = yValues[i][0].value - slopeValues[i][0].value*xValues[i][0].value
            outputValues.append([timeValues[i][0].value, slopeValues[i][0].value, intercept])
      

    return outputValues
