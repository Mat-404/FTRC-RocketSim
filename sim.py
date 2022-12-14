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
  
  def getMagnitude(tuple1, timeStep, time):
    temp = 0
    try: temp = math.sqrt(tuple1[0]**2+tuple1[1]**2+tuple1[2]**2)
    except: 
      print(f"Overflow error at t={timeStep*time}s")
      print(f"Tuple: {tuple1}")
    return temp

  def getOrientation(tuple1, tuple2, timeStep, time):
    try: a = math.sqrt((tuple2[0]-tuple1[0])**2+(tuple2[1]-tuple1[1])**2+(tuple2[2]-tuple1[2])**2)
    except: 
      print(f"Overflow error at t={timeStep*time}s")
      print(f"Tuple: {tuple1}")
      a = 0
    b = (abs(tuple2[0]-tuple1[0]), abs(tuple2[1]-tuple1[1]), abs(tuple2[2]-tuple1[2]))
    return divideTuple(b,a)

  def getUnitVector(tuple):
    a = math.sqrt(tuple[0]**2+tuple[1]**2+tuple[2]**2)
    return (tuple[0]/a, tuple[1]/a, tuple[2]/a)

  def getThreeDimensionalSlope(tuple1, tuple2):
    temp = math.sqrt((tuple1[0]-tuple2[0])**2+(tuple1[1]-tuple2[1])**2+(tuple1[2]-tuple2[2])**2)
    return (divideTuple((tuple1[0]-tuple2[0],tuple1[1]-tuple2[1],tuple1[2]-tuple2[2]),temp))

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

  def createThreeDimensionalFigure(numberOfEngines, EngineChoice, payloadMass, positionPoints):
    fig = plt.figure(facecolor='#390505')
    ax = plt.axes(projection='3d')
    xVals = []
    yVals = []
    zVals = []
    xLand = 0
    yLand = 0
    for i in positionPoints:
      xVals.append(i[0])
      yVals.append(i[1])
      zVals.append(i[2])
    
    # remove points that have a zValue less than 0
    for i in range(len(zVals)):
      if zVals[i] < 0 and i > 1000:
        xVals = xVals[:i]
        yVals = yVals[:i]
        zVals = zVals[:i]
        xLand = xVals[-1]
        yLand = yVals[-1]
        break

    ax.plot3D(xVals, yVals, zVals)
    ax.set_title(f'Rocket Simulation for {str(int(numberOfEngines))} {EngineChoice} Engines\n and a payload of {str(payloadMass)} kg')

    return fig, xLand, yLand

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
    positionPoints = []
    orientationList = []

    ##   Zeroing Variables   ##
    burnedMass = 0
    dragNewtons = 0
    densityPascals = 0
    positionTuple = (0,0,0)
    launchVector = (math.cos(math.radians(pitchAngle))*math.cos(math.radians(azimuthAngle)), math.cos(math.radians(pitchAngle))*math.sin(math.radians(azimuthAngle)), math.sin(math.radians(pitchAngle)))
    orientationTuple = launchVector
    thrustTuple = (0,0,0)
    accelerationTuple = (0,0,0)
    velocityTuple = (0,0,0)
    

    pitchAngle = math.radians(pitchAngle)
    azimuthAngle = math.radians(azimuthAngle)

    thrustCurve = tca.main(EngineChoice)

    #### Main Loop ####
    for i in range(0, int(timeLimitSeconds/timeStepSeconds)):

      if burnedMass < propellantMassKilograms:
          currentMass = initialMassKilograms-burnedMass        
      
      if positionTuple[2] < 0 and i < 100:
        positionTuple = (positionTuple[0], positionTuple[1], 0.0)

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
      
      dragNewtons = coeffDrag*(densityPascals*getMagnitude(velocityTuple, timeStepSeconds, i)**2)/2*crossSectionalArea  # Newtons

      dragTuple = multiplyTuple(multiplyTuple(orientationTuple,-1), dragNewtons)

      dynamicPressureList.append((1/2)*densityPascals*getMagnitude(velocityTuple, timeStepSeconds, i)**2)

        ######  This is where the kinematics are calculated  ######
      
      accelerationTuple = addTuple(divideTuple(addTuple(thrustTuple, dragTuple), currentMass), (0,0,-9.7918))
      
      velocityTuple = addTuple(velocityTuple, multiplyTuple(accelerationTuple, timeStepSeconds))
      
      positionTuple = addTuple(positionTuple, multiplyTuple(velocityTuple, timeStepSeconds))
      
      burnedMass = burnedMass+burnRateKgS*(1*timeStepSeconds)

      ######  This is where the data is stored  ######
      timeList.append(int(i))
      altitudeList.append(positionTuple[2])
      thrustList.append(getMagnitude(thrustTuple, timeStepSeconds, i))
      velocityList.append(np.dot(velocityTuple, orientationTuple))
      accelerationList.append(np.dot(accelerationTuple, orientationTuple))
      positionPoints.append(positionTuple)
      orientationList.append(orientationTuple)

      orientationTuple = getUnitVector(
        addTuple(orientationTuple, 
        getOrientation(multiplyTuple(launchVector, -1), positionPoints[-1], timeStepSeconds, i)))
      

    figType = "3D"

    if figType == "2D":
      fig = createTwoDimensionalFigure(numberOfEngines, EngineChoice, payloadMass, timeList, altitudeList, velocityList, thrustList, accelerationList)
      xLand = ''
      yLand = ''
    elif figType == "3D":
      output = createThreeDimensionalFigure(numberOfEngines, EngineChoice, payloadMass, positionPoints)
      fig = output[0]
      xLand = output[1]
      yLand = output[2]
    """
    for i in range(0, round(len(accelerationList)*.6)):
      print (f"Orientation: {accelerationList[i]}")
    """
    return timeList, altitudeList, velocityList, thrustList, accelerationList, dynamicPressureList, xLand, yLand, fig
