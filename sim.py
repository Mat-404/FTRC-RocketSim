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
import matplotlib
from openpyxl import load_workbook
from os.path import exists

DataWorkbook = load_workbook("Mk1 Data Sheet.xlsx")
EngineData = DataWorkbook["Engines"]

if exists("coconut.jpg"):

  ## TODO: Add a way to choose between NAR data and own data ##
  
  def calculateSim(EngineChoice, timeStepSeconds, timeLimitSeconds, payloadMass, numberOfEngines):
    
    ##  Importing data from spreadsheet ##
    ##  engine choice corresponds to column in spreadsheet ##
    if EngineChoice == "D12":
      columnVar = 'B'
    elif EngineChoice == "F15":
      columnVar = 'G'
    elif EngineChoice == "H13":
      columnVar = 'K'

        ##  Defining variables ##
    initialMassKilograms = (EngineData[columnVar+'11'].value+EngineData[columnVar+'12'].value)*numberOfEngines + payloadMass + EngineData[columnVar+'21'].value  # kg
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
    velocityMetersSquared = 0
    currentAltitudeMeter = 0
    dragNewtons = 0
    densityPascals = 0
    currentThrustNewtons = 0


    thrustCurve = tca.main(EngineChoice)

    

    #### Main Loop ####
    for i in range(0, int(timeLimitSeconds/timeStepSeconds)):
      if burnedMass < propellantMassKilograms:
          currentMass = initialMassKilograms-burnedMass

        ### Calculating Thrust from curve ###
      for j in thrustCurve:
        if j[0] >= i*timeStepSeconds:
          currentThrustNewtons = (j[1]*(i*timeStepSeconds)+j[2])*numberOfEngines
          break
        else:
          currentThrustNewtons = 0
        

        ######  This is where the drag is calculated  ######
      if currentAltitudeMeter < 11019.13:
          # (Assuming linear density change under 1km)
          densityPascals = 1.225-(0.000113*currentAltitudeMeter)
      dragNewtons = coeffDrag*(densityPascals*velocityMetersSquared**2)/2*crossSectionalArea  # Newtons

      dynamicPressureList.append((1/2)*densityPascals*velocityMetersSquared**2)

        ######  This is where the kinematics are calculated  ######
      acceleration = (currentThrustNewtons-dragNewtons)/currentMass-9.7918
      velocityMetersSquared = velocityMetersSquared+acceleration*timeStepSeconds
      currentAltitudeMeter = currentAltitudeMeter+velocityMetersSquared*timeStepSeconds
      burnedMass = burnedMass+burnRateKgS*(1*timeStepSeconds)

      ######  This is where the data is stored  ######
      timeList.append(int(i))
      altitudeList.append(currentAltitudeMeter)
      thrustList.append(currentThrustNewtons)
      velocityList.append(velocityMetersSquared)
      accelerationList.append(acceleration)
    
    ##### Plotting #####
    fig, axis = plt.subplots(2,2)
    fig.suptitle('Rocket Simulation for '+str(int(numberOfEngines))+" "+EngineChoice+' Engines\n and a payload of '+str(payloadMass)+' kg')

    index = altitudeList.index(max(altitudeList))
    a = len(altitudeList)-index
    for i in range(0, a):
      altitudeList.pop()
      velocityList.pop()
      accelerationList.pop()
      timeList.pop()
      thrustList.pop()
      dynamicPressureList.pop()

    axis[0,0].plot(timeList, altitudeList)
    axis[0,0].set_title("Height vs Time")
    axis[0,1].plot(timeList, velocityList)
    axis[0,1].set_title("Velocity vs Time")
    axis[1,0].plot(timeList, thrustList)
    axis[1,0].set_title("Thrust vs Time")
    axis[1,1].plot(timeList, accelerationList)
    axis[1,1].set_title("Acceleration vs Time")
    
    return timeList, altitudeList, velocityList, thrustList, accelerationList, dynamicPressureList, fig
