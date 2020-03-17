import sys
import math
# /Applications/VisIt.app/Contents/Resources/bin/visit -cli -s vpandv.py

# Path for Alyssa's aneurysm data:
#path_to_aneurysm_data = "localhost:/Users/alyssakelley/scientific_visualization/aneurysm_data/aneurysm_data/"

# Path for Anne's aneurysm data:
path_to_aneurysm_data = "localhost:/Users/moonshine/CIS_410/finalproject/scientific_visualization/aneurysm_data/"


def SetUpVPV():
    RestoreSession("vpandv.session",0)
    OpenDatabase(path_to_aneurysm_data + "aneurysm.visit", 0)
    AddPlot("Volume", "pressure", 1, 1)
    AddPlot("Contour", "velocity_magnitude", 1, 1)
    DrawPlots()

def AnimateInTime():
    for i in range(350):
        TimeSliderSetState(i)
        SaveWindow()

def AnimateAroundZAxis():
   v = GetView3D()
   v.viewNormal = (0.357003, 0.628678, 0.690879)
   v.focus = (0.292, 0.292, 0.219)
   v.viewUp = (0, 0, 1)
   v.viewAngle = 30
   v.parallelScale = 0.467428
   v.nearPlane = -0.934856
   v.farPlane = 0.934856
   v.imagePan = (0, 0)
   v.imageZoom = 1
   v.perspective = 1
   v.eyeAngle = 2
   v.centerOfRotationSet = 0
   v.centerOfRotation = (0.292, 0.292, 0.219)
   v.axis3DScaleFlag = 0
   v.axis3DScales = (1, 1, 1)
   v.shear = (0, 0, 1)
   v.windowValid = 1
   for i in range(50):
       angle = 3.14159 * 2 * i/49.0
       v.viewNormal = (math.cos(angle), math.sin(angle), 0)
       SetView3D(v)

def main():
    SetUpVPV()
    #AnimateAroundZAxis()
    AnimateInTime()
    sys.exit()