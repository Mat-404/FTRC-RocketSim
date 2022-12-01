    ###################################################
    #                                                 #
    #   Boilerplate GUI and User Input                #
    #                                                 #
    ###################################################

    ##  Importing libraries and spreadsheet ##
import sim as sim
import optimizeSubroutine as OST
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
import matplotlib
import os
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageGrab

matplotlib.rcParams['text.color'] = '#F6C350'
matplotlib.rcParams['axes.labelcolor'] = '#F6C350'
matplotlib.rcParams['xtick.color'] = '#F6C350'
matplotlib.rcParams['ytick.color'] = '#F6C350'

sg.theme('DarkBrown5')   # Add that fresh Florida Tech color scheme

matplotlib.use('TkAgg')

def sysRestart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

   ##  Setting up GUI ##

column_1 = [[sg.Image(filename = 'Rocketry_Club_Logo.png', key='-IMAGE-')]]
column_2 = [[sg.Text("Welcome to the FTRC Rocket Simulator!")],
            [sg.Text("This is a work in progress, so please be patient.")],
            [sg.Text("Choose which engine you want to use:")],
            [sg.Button("D12"), sg.Button("F15"), sg.Button("H13")], 
            [sg.Text("Optimize for: "), sg.InputText()],
            [sg.Text("Compare up to how many engines: "), sg.InputText()],
            [sg.Button("Edit Rocket Data Sheet", key="editData")],
            [sg.Button("Edit Engine Database", key="editEngine")]]

layout = [[sg.Column(column_1),
           sg.Column(column_2)]]

window1 = sg.Window("FTRC Rocketry Sim", layout, finalize=True)

window1.force_focus()

event, values = window1.read()

if event == "editData":
    os.startfile("Mk1 Data Sheet.xlsx")
    window1.close()
    sysRestart()

if event == "editEngine":
    os.startfile("EngineDataSheet.xlsx")
    window1.close()
    sysRestart()

if event == "D12" or event == "F15":
    timeLimitSeconds = 10  # seconds
    timeStepSeconds = .001  # seconds
elif event == "H13":
    timeLimitSeconds = 30  # seconds
    timeStepSeconds = .001  # seconds
elif event == sg.WIN_CLOSED:
    window1.close()
    sys.exit()


#if (values[0].isalpha() or float(values[0]) < 0):
#    sg.popup("Please enter a valid payload mass")
#    sysRestart()
#if (values[1].isalpha() or int(values[1]) <= 0):
#    sg.popup("Please enter a valid number of engines")
#    sysRestart()

optimizedValues = OST.optimize(event, timeStepSeconds, timeLimitSeconds, values[0], int(values[1]))
window1.close()

fig, axis = plt.subplots(2,2)
fig.suptitle('Engine Number optimized for '+values[0]+": \nOptimized Engine Number: "+str(optimizedValues[0]))
timeList = optimizedValues[1]
altitudeList = optimizedValues[2]
velocityList = optimizedValues[3]
thrustList = optimizedValues[4]
accelerationList = optimizedValues[5]
dynamicPressureList = optimizedValues[6]
maxHeightTime = altitudeList.index(max(altitudeList))/1000

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

column_1=[[sg.Canvas(key='-CANVAS2')]]

column_2=[[sg.Text("Maximum Velocity: " + str(max(altitudeList))+ " m/s")],
            [sg.Text("Maximum Height: " + str(max(altitudeList))+ " m")],
            [sg.Text("Time to peak: " + str(maxHeightTime)+ " s")],
            [sg.Text("Maximum Thrust: " + str(max(thrustList)) + " N")],
            [sg.Text("Maximum Acceleration: " + str(max(accelerationList))+ " m/s^2")],
            [sg.Text("Maximum Dynamic Pressure: " + str(max(dynamicPressureList))+ " N/m^2")],
            [sg.Text("Maximum Mach Number: " + str(round(max(velocityList)/343,3)))],
            [sg.Button('Reset', size=(14, 1))]]

layout = [[sg.Column(column_1),
           sg.Column(column_2)]]

window2 = sg.Window("FTRC Rocketry Sim", layout, finalize=True)

fig_canvas_agg = draw_figure(window2["-CANVAS2"].TKCanvas, fig)

event, values = window2.read()

if event == "Reset":
    sysRestart()