import sys
# /Applications/VisIt.app/Contents/Resources/bin/visit -cli -s velocity.py

# Path for Alyssa's aneurysm data:
path_to_aneurysm_data = "localhost:/Users/alyssakelley/scientific_visualization/aneurysm_data/aneurysm_data/"

# Path for Anne's aneurysm data:
# path_to_aneurysm_data = "localhost:/Users/moonshine/CIS_410/finalproject/aneurysm_tutorial_data/aneurysm_data/"

def SetUpVelocity():
    #RestoreSession("velocity.session",0)
    RestoreSession("vandp2.session",0)
    OpenDatabase(
    path_to_aneurysm_data+"aneurysm*.silo database",0)
    AddPlot("Contour", "velocity_magnitude", 1, 1)
    DrawPlots()

def AnimateInTime():
    for i in range(50):
        TimeSliderSetState(i)
        #SaveWindow()

def main():
	SetUpVelocity()
	AnimateInTime()
	sys.exit()