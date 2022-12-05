###################################################
#                                                 #
#   Rocket Simulation                             #
#                                                 #
#   Taking into account air resistance            #
#   varying mass, and thrust                      #
#                                                 #
#                                                 #
###################################################

    ##  Importing libraries and spreadsheet ##
import thrustCurveAnalysis_UPDATED as tca
import matplotlib.pyplot as plt
import openpyxl
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib
import math
from openpyxl import load_workbook
from os.path import exists

DataWorkbook = load_workbook("Mk1 Data Sheet.xlsx")
EngineData = DataWorkbook["Engines"]

if exists("coconut.jpg"):

  columnVar = ''

  def addTuple(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))
  
  def multiplyTuple(tuple1, scalar):
    return tuple(map(lambda x: x*scalar, tuple1))
  
  def divideTuple(tuple1, scalar):
    return tuple(map(lambda x: x/scalar, tuple1))
  
  def getMagnitude(tuple1):
    return math.sqrt(tuple1[0]**2+tuple1[1]**2+tuple1[2]**2)
  
  def getThreeDimensionalSlope(tuple1, tuple2):
    return divideTuple(addTuple(tuple1, tuple2), 2)

  def assignDataVariables(EngineChoice):
    if EngineChoice == "D12":
      columnVar = 'B'
    elif EngineChoice == "F15":
      columnVar = 'G'
    elif EngineChoice == "H13":
      columnVar = 'K'
    elif EngineChoice == "E12":
      columnVar = 'O'
    return columnVar

  def getInitialMass(EngineChoice, numberOfEngines, payloadMass):
    columnVar = assignDataVariables(EngineChoice)
    return (EngineData[columnVar+'11'].value+EngineData[columnVar+'12'].value)*numberOfEngines + payloadMass + EngineData[columnVar+'21'].value  # kg
  
  def createTwoDimensionalFigure(numberOfEngines, EngineChoice, payloadMass, timeList, altitudeList, velocityList, thrustList, accelerationList):
    ##### Plotting #####
    fig, axis = plt.subplots(2,2)
    fig.suptitle(f'Rocket Simulation for {str(int(numberOfEngines))} {EngineChoice} Engines\n and a payload of {str(payloadMass)} kg')

    axis[0,0].plot(timeList, altitudeList)
    axis[0,0].set_title("Height vs Time")
    axis[0,1].plot(timeList, velocityList)
    axis[0,1].set_title("Velocity vs Time")
    axis[1,0].plot(timeList, thrustList)
    axis[1,0].set_title("Thrust vs Time")
    axis[1,1].plot(timeList, accelerationList)
    axis[1,1].set_title("Acceleration vs Time")

    fig.set_edgecolor('#F6C370')
    fig.set_facecolor('#3C1B1F')
    fig.tight_layout()

    return fig

  def createThreeDimensionalFigure(numberOfEngines, EngineChoice, payloadMass, timeList, altitudeList, velocityList, thrustList, accelerationList):
    fig = plt.figure(facecolor='#390505')
    ax = plt.axes(projection='3d')
    xVals = []
    yVals = []
    for i in range (0,len(altitudeList)):
      xVals.append(0)
      yVals.append(0)
    ax.plot3D(xVals, yVals, altitudeList)
    ax.set_title(f'Rocket Simulation for {str(int(numberOfEngines))} {EngineChoice} Engines\n and a payload of {str(payloadMass)} kg')

    return fig

  def calculateSim(EngineChoice, timeStepSeconds, timeLimitSeconds, payloadMass, numberOfEngines, pitchAngle, azimuthAngle):
    
    ##  Importing data from spreadsheet ##
    ##  engine choice corresponds to column in spreadsheet ##
    columnVar = assignDataVariables(EngineChoice)

    initialMassKilograms = getInitialMass(EngineChoice, numberOfEngines, payloadMass)  # kg
    propellantMassKilograms = EngineData[columnVar+'12'].value*numberOfEngines  # kg
    burnRateKgS = propellantMassKilograms / (EngineData[columnVar+'10'].value)  # burnRate in kg/s
    angle = 14.04952  # Angle between edge and center of cone in degrees
    crossSectionalArea = 3.14*(0.305/2)**2  # m^2
    coeffDrag = 0.0112*angle+0.162  # drag coefficient





    ##   Initializing Arrays   ##
    timeList = []
    thrustList = []
    accelerationList = []
    velocityList = []
    altitudeList = []
    dynamicPressureList = []
    thrustCurve = []

    ##   Zeroing Variables   ##
    burnedMass = 0
    dragNewtons = 0
    densityPascals = 0
    positionTuple = (0,0,0)
    orientationTuple = (math.cos(pitchAngle)*math.cos(azimuthAngle), math.cos(pitchAngle)*math.sin(azimuthAngle), math.sin(pitchAngle))
    thrustTuple = (0,0,0)
    accelerationTuple = (0,0,0)
    velocityTuple = (0,0,0)
    previousPositionTuple = (0,0,0)
    

    pitchAngle = math.radians(pitchAngle)
    azimuthAngle = math.radians(azimuthAngle)

    thrustCurve = tca.main(EngineChoice)

    #### Main Loop ####
    for i in range(0, int(timeLimitSeconds/timeStepSeconds)):
      if burnedMass < propellantMassKilograms:
          currentMass = initialMassKilograms-burnedMass

      if orientationTuple[2] < 0 and i < 1:
        orientationTuple[2] = 0
        break
      
      if positionTuple[2] < 0:
        positionTuple = (positionTuple[0], positionTuple[1], 0)

      if positionTuple[2] < -1:
        break

        ### Calculating Thrust from curve ###
      for j in thrustCurve:
        if j[0] >= i*timeStepSeconds:
          currentThrustNewtons = (j[1]*(i*timeStepSeconds)+j[2])*numberOfEngines
          break
        else:
          currentThrustNewtons = 0
      
      thrustTuple = multiplyTuple(orientationTuple, currentThrustNewtons)
        
        ######  This is where the drag is calculated  ######
      if positionTuple[2] < 11019.13:
          # (Assuming linear density change under 1km)
          try: densityPascals = 1.225-(0.000113*positionTuple[2])
          except OverflowError:
            densityPascals = 0
          #finally:
            #print (f"Overflow Error Log, time at {i*timeStepSeconds} seconds")
            #print (f"Current Altitude: {currentAltitudeMeter}")
      dragNewtons = coeffDrag*(densityPascals*getMagnitude(velocityTuple)**2)/2*crossSectionalArea  # Newtons

      dragTuple = multiplyTuple(multiplyTuple(orientationTuple,-1), dragNewtons)

      dynamicPressureList.append((1/2)*densityPascals*getMagnitude(velocityTuple)**2)

        ######  This is where the kinematics are calculated  ######
      #acceleration = (currentThrustNewtons-dragNewtons)/currentMass-9.7918
      
      accelerationTuple = addTuple(divideTuple(addTuple(thrustTuple, dragTuple), currentMass), (0,0,-9.7918))
      
      #velocityMetersSquared = velocityMetersSquared+acceleration*timeStepSeconds
      
      velocityTuple = addTuple(velocityTuple, multiplyTuple(accelerationTuple, timeStepSeconds))
      
      #currentAltitudeMeter = currentAltitudeMeter+velocityMetersSquared*timeStepSeconds
      
      positionTuple = addTuple(positionTuple, multiplyTuple(velocityTuple, timeStepSeconds))
      
      #altitudeTuple = addTuple(altitudeTuple, multiplyTuple(velocityTuple, timeStepSeconds))
      
      burnedMass = burnedMass+burnRateKgS*(1*timeStepSeconds)

      ######  This is where the data is stored  ######
      timeList.append(int(i))
      altitudeList.append(positionTuple[2])
      thrustList.append(getMagnitude(thrustTuple))
      velocityList.append(getMagnitude(velocityTuple))
      accelerationList.append(getMagnitude(accelerationTuple))
      
      previousPositionTuple = positionTuple
      
      orientationTuple = getThreeDimensionalSlope(previousPositionTuple, positionTuple)
      
    
    ## Remove entries after a time length after maximum height ##
    
    for i in range(0, round(len(altitudeList)-(altitudeList.index(max(altitudeList)))*1.3 )):
      altitudeList.pop()
      velocityList.pop()
      accelerationList.pop()
      timeList.pop()
      thrustList.pop()
      dynamicPressureList.pop()

    figType = "3D"

    if figType == "2D":
      fig = createTwoDimensionalFigure(numberOfEngines, EngineChoice, payloadMass, timeList, altitudeList, velocityList, thrustList, accelerationList)
    elif figType == "3D":
      fig = createThreeDimensionalFigure(numberOfEngines, EngineChoice, payloadMass, timeList, altitudeList, velocityList, thrustList, accelerationList)


    return timeList, altitudeList, velocityList, thrustList, accelerationList, dynamicPressureList, fig
