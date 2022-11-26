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
import matplotlib.pyplot as plt
import openpyxl
from openpyxl import load_workbook
wb = load_workbook("Mk1 Data Sheet.xlsx")
Engines = wb["Engines"]
Dims = wb["Volume Calculations"]

    ##  Defining variables ##
numberOfEngines = Engines['D2'].value
initialMass = (Engines['B13'].value + Engines['B14'].value) * \
    Engines['D2'].value + Engines['B22'].value + Engines['D20'].value  # kg
propellantMass = Engines['B14'].value*numberOfEngines  # kg
burnRate = propellantMass / (Engines['B10'].value)  # burnRate in kg/s
timeLimit = 12  # seconds
timeStep = .001  # seconds
angle = 14.04952  # Angle between edge and center of cone in degrees

#print("Initial Mass: ", round(initialMass, 2), "propellantMass: ",
#      round(propellantMass, 2), "burnRate: ", round(burnRate, 2))

crossSectionalArea = 3.14*(0.305/2)**2  # m^2
coeffDrag = 0.0112*angle+0.162  # drag coefficient

##   Initializing Arrays   ##
time = [None]*int(timeLimit/timeStep)
Thrust = [None]*int(timeLimit/timeStep)
accel = [None]*int(timeLimit/timeStep)
Vel = [None]*int(timeLimit/timeStep)
height = [None]*int(timeLimit/timeStep)


##   Zeroing Variables   ##
burnedMass = 0
velocity = 0
distance = 0
maxHeight = 0
maxVel = 0
Drag = 0
density = 0
temperature = 0
pressure = 0
thrust = 0


  #### Main Loop ####
for i in range(0, int(timeLimit/timeStep)):
    if burnedMass < propellantMass:
        currentMass = initialMass-burnedMass


      ######  This is where the thrust is calculated  ######
    if i >= 0 and i < 0.282/timeStep:
        thrust = (105.425*(i*timeStep))*numberOfEngines
    elif i >= 0.282/timeStep and i < 0.386/timeStep:
        thrust = (76.89-167.54*(i*timeStep))*numberOfEngines
    elif i >= 0.386/timeStep and i < 1.436/timeStep:
        thrust = (12.099-0.00567*(i*timeStep))*numberOfEngines
    elif i >= 1.436/timeStep and i < 1.556/timeStep:
        thrust = (155.91-100.23*(i*timeStep))*numberOfEngines
    else:
        thrust = 0


      ######  This is where the drag is calculated  ######
    if distance < 11019.13:
        # (Assuming linear density change under 1km)
        density = 1.225-0.000113*distance
    Drag = coeffDrag*(density*velocity**2)/2*crossSectionalArea  # Newtons


      ######  This is where the kinematics are calculated  ######
    acceleration = (thrust-Drag)/currentMass-9.8
    velocity = velocity+acceleration*timeStep
    distance = distance+velocity*timeStep
    burnedMass = burnedMass+burnRate*(1*timeStep)

      ######  This is where the max values are stored  ######
    if velocity > maxVel:
        maxVel = velocity
    if distance > maxHeight:
        maxHeight = distance


      ######  This is where the data is stored  ######
    time[i] = i
    height[i] = distance
    Thrust[i] = thrust
    Vel[i] = velocity
    accel[i] = acceleration

  ##### List maximums #####
print("Max Height: ", round(maxHeight, 3), "m",
      "Max Velocity: ", round(maxVel, 3), "m/s")

  ##### Plotting #####
fig, axis = plt.subplots(2,2)

fig.suptitle('Max Height: '+str(round(maxHeight, 3))+'m Max Velocity: '+str(round(maxVel, 3))+'m/s')

axis[0,0].plot(time, height)
axis[0,0].set_title("Height vs Time")
axis[0,1].plot(time, Vel)
axis[0,1].set_title("Velocity vs Time")
axis[1,0].plot(time, Thrust)
axis[1,0].set_title("Thrust vs Time")
axis[1,1].plot(time, accel)
axis[1,1].set_title("Acceleration vs Time")

plt.show()