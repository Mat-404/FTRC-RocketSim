###################################################
#                                                 #
#   Boilerplate GUI and User Input                #
#                                                 #
###################################################

    ##  Importing libraries and spreadsheet ##
import sim as sim
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
import matplotlib
import os
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


matplotlib.rcParams['text.color'] = '#F6C350'
matplotlib.rcParams['axes.labelcolor'] = '#F6C350'
matplotlib.rcParams['xtick.color'] = '#F6C350'
matplotlib.rcParams['ytick.color'] = '#F6C350'

sg.theme('DarkBrown5')   # Add that fresh Florida Tech color scheme

matplotlib.use('TkAgg')

def sysRestart():
    os.execl(sys.executable, sys.executable, *sys.argv)

   ##  Setting up GUI ##

column_1 = [[sg.Image(filename = 'Rocketry_Club_Logo.png', key='-IMAGE-')]]
column_2 = [[sg.Text("Welcome to the FTRC Rocket Simulator!")],
            [sg.Text("This is a work in progress, so please be patient.")],
            [sg.Text("Choose which engine you want to use:")],
            [sg.Button("D12"), sg.Button("F15"), sg.Button("H13"), sg.Button("E12")], 
            [sg.Text("Payload Mass (Kg): "), sg.InputText(size=(15,1)), sg.Text("Pitch Angle (Deg): "), sg.InputText(size=(17,1))],
            [sg.Text("Number of Engines: "), sg.InputText(size=(15,1)), sg.Text("Azimuth Angle (Deg): "), sg.InputText(size=(15,1))],
            [sg.Button("Edit Rocket Data Sheet", key="editData")],
            [sg.Button("Edit Engine Database", key="editEngine")]]

layout = [[sg.Column(column_1),
           sg.Column(column_2)]]

window1 = sg.Window('FTRC Rocket Simulator', layout, finalize=True)

window1.force_focus()

event, values = window1.read()
maxThrust = 0

payloadMass=values[0]
pitchAngle=values[1]
numberOfEngines=values[2]
azimuthAngle=values[3]

if event == "editData":
    os.startfile("Mk1 Data Sheet.xlsx")
    window1.close()
    sysRestart()
elif event == "editEngine":
    os.startfile("EngineDataSheet.xlsx")
    window1.close()
    sysRestart()
elif event == "D12":
    timeLimitSeconds = 10  # seconds
    timeStepSeconds = .001  # seconds
    maxThrust = 32.9  # Newtons
elif event == "F15":
    timeLimitSeconds = 10  # seconds
    timeStepSeconds = .001  # seconds
    maxThrust = 25.26  # Newtons
elif event == "H13":
    timeLimitSeconds = 45  # seconds
    timeStepSeconds = .001  # seconds
    maxThrust = 43.5  # Newtons
elif event == "E12":
    timeLimitSeconds = 10  # seconds
    timeStepSeconds = .001 # seconds
    maxThrust = 30.6 # Newtons
elif event == sg.WIN_CLOSED:
    window1.close()
    sys.exit()


if (payloadMass.isalpha() or float(payloadMass) < 0):
    sg.popup("Please enter a valid payload mass")
    sysRestart()
if (numberOfEngines.isalpha() or int(numberOfEngines) <= 0):
    sg.popup("Please enter a valid number of engines")
    sysRestart()

initialMass = sim.getInitialMass(event, float(values[0]), int(values[1]))
if ((maxThrust*float(values[1]))/(initialMass*9.81) < 1):
    sg.popup("Warning: TWR < 1")
    sysRestart()

simResults = sim.calculateSim(event, timeStepSeconds, timeLimitSeconds, float(payloadMass), float(numberOfEngines), float(pitchAngle), float(azimuthAngle))
fig = simResults[-1]

timeValues = simResults[0]
heightValues = simResults[1]

maxHeight = round(max(simResults[1]),3)
maxHeightTime = heightValues.index(max(simResults[1]))/1000
maxVelocity = round(max(simResults[2]),3)
maxThrust = str(round(max(simResults[3]),3))
maxAcceleration = str(round(max(simResults[4]),3))
maxQ = str(round(max(simResults[5]),3))

window1.close()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

column_1=[[sg.Canvas(key='-CANVAS2')]]

column_2=[[sg.Text(f"Maximum Velocity: {str(maxVelocity)} m/s")],
            [sg.Text(f"Maximum Height: {str(maxHeight)} m")],
            [sg.Text(f"Time to peak: {str(maxHeightTime)} s")],
            [sg.Text(f"Maximum Thrust: {maxThrust} N")],
            [sg.Text(f"Maximum Acceleration: {maxAcceleration} m/s^2")],
            [sg.Text(f"Maximum Dynamic Pressure: {maxQ} N/m^2")],
            [sg.Text(f"Maximum Mach Number: {str(round(maxVelocity/343,3))}")],
            [sg.Button('Reset', size=(14, 1))]]

layout = [[sg.Column(column_1),
           sg.Column(column_2)]]

window2 = sg.Window("FTRC Rocketry Sim", layout, finalize=True)

fig_canvas_agg = draw_figure(window2["-CANVAS2"].TKCanvas, fig)

event, values = window2.read()

if event == "Reset":
    sysRestart()