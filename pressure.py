import sys
# /Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pressure.py

# Path for Alyssa's aneurysm data:
#path_to_aneurysm_data = "localhost:/Users/alyssakelley/scientific_visualization/aneurysm_data/aneurysm_data/"

# Path for Anne's aneurysm data:
path_to_aneurysm_data = "localhost:/Users/moonshine/CIS_410/finalproject/aneurysm_tutorial_data/aneurysm_data/"

def SetUpPressure():
    #RestoreSession("pressure.session",0)
    RestoreSession("pressure.session",0)
    OpenDatabase(
    path_to_aneurysm_data+"aneurysm*.silo database",0)
    AddPlot("Contour", "pressure", 1, 1)
    DrawPlots()

def AnimateInTime():
    for i in range(50):
        TimeSliderSetState(i)
        #SaveWindow()

def main():
	SetUpPressure()
	AnimateInTime()
	sys.exit()