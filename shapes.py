import math
import PySimpleGUI as sg

numberOfEngines = 10
engineInsetPercent = 0.5

class cylinder:
    def __init__(self, radius, height, orientation, xOffset, yOffset):
        self.radius = radius
        self.height = height
        self.orientation = orientation
        self.shapeType = "cylinder"
        self.xOffset = xOffset
        self.yOffset = yOffset
    def volume(self):
        return math.pi * self.radius ** 2 * self.height
    def surface_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2
    def getOrientation(self):
        return self.orientation
    def getShapeType(self):
        return self.shapeType

class TruncatedCone:
    def __init__(self, bottomRadius, topRadius, height, orientation, xOffset, yOffset):
        self.bottomRadius = bottomRadius
        self.height = height
        self.topRadius = topRadius
        self.orientation = orientation
        self.shapeType = "truncatedCone"
        self.xOffset = xOffset
        self.yOffset = yOffset
    def volume(self):
        return (1/3) * math.pi * self.height * (self.bottomRadius**2 + self.bottomRadius*self.topRadius + self.topRadius**2)
    def surface_area(self):
        return math.pi * self.topRadius**2+(math.pi*self.radius**2-math.pi*self.topRadius**2)
    def getOrientation(self):
        return self.orientation
    def getShapeType(self):
        return self.shapeType

class Cone:
    def __init__(self, radius, height, orientation, xOffset, yOffset):
        self.radius = radius
        self.height = height
        self.orientation = orientation
        self.shapeType = "cone"
        self.xOffset = xOffset
        self.yOffset = yOffset
    def volume(self):
        return math.pi * self.radius ** 2 * self.height / 3
    def surface_area(self):
        return math.pi * self.radius **2
    def getOrientation(self):
        return self.orientation
    def getShapeType(self):
        return self.shapeType

sg.theme('DarkBrown5')

column_1 = [[sg.Image(filename = 'Rocketry_Club_Logo.png', key='-IMAGE-')]]
column_2 = [[sg.Text("Welcome to the FTRC Rocket Designer!")],
            [sg.Text("This is a work in progress, so please be patient.")]]
layout = [[sg.Column(column_1),
           sg.Column(column_2)]]
window1 = sg.Window('FTRC Rocket Designer', layout, finalize=True)
window1.force_focus()
event, values = window1.read()

mainBody = Cone(0.1525, 0.610, "horizontal", 50, 0)
payloadBay = TruncatedCone(0.147, 0.056, 0.293, "horizontal", 0, 0)
totalEngineVolume=0
shapes = [cylinder(0.015, 0.11, "horizontal", 0, 0) for i in range(3)]
for obj in shapes:
    totalEngineVolume += obj.volume()
shapes.append(mainBody)
shapes.append(payloadBay)

print(f"Body Volume: {round(mainBody.volume(),5)}m^3")
print(f"Payload Bay Volume: {round(payloadBay.volume(),5)}m^3")
print(f"Engine Volume: {round(totalEngineVolume,5)}m^3")
print (f"Total Airframe Volume: {round(mainBody.volume()-payloadBay.volume()-totalEngineVolume*engineInsetPercent,5)}m^3")

print("\n")
window1.close
window1.close()