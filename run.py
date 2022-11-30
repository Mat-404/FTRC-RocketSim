    ##  Importing libraries and spreadsheet ##
import sim as sim
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import os
import sys

sg.theme('DarkBrown5')   # Add a touch of color

matplotlib.use('TkAgg')

   ##  Setting up GUI ##
window1 = sg.Window(title="FTRC Rocketry Sim", 
        layout=[[sg.Text("Choose which engine you want to use")],
        [sg.Button("D12")],[sg.Button("F15")], [sg.Canvas(key="-CANVAS")]], margins=(200, 50))

event, values = window1.read()
print(event)

simResults = sim.calcuateSim(event)
fig = simResults[7]
maxHeight = str(simResults[0])
maxVelocity = str(simResults[1])

window1.close()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

column_1=[[sg.Canvas(key='-CANVAS2')]]

column_2=[[sg.Text("Maximum Velocity: " + maxVelocity)],
            [sg.Text("Maximum Height: " + maxHeight)],
            [sg.Button('Reset', size=(14, 1))]]

layout = [[sg.Column(column_1),
           sg.Column(column_2)],]

window2 = sg.Window("FTRC Rocketry Sim", layout, margins=(200, 50), finalize=True)

fig_canvas_agg = draw_figure(window2["-CANVAS2"].TKCanvas, fig)

event, values = window2.read()
print(event)

if event == "Reset":
    os.execl(sys.executable, sys.executable, *sys.argv)