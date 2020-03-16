import sys
# /Applications/VisIt.app/Contents/Resources/bin/visit -cli -s vpandv.py

# Path for Alyssa's aneurysm data:
#path_to_aneurysm_data = "localhost:/Users/alyssakelley/scientific_visualization/aneurysm_data/aneurysm_data/"

# Path for Anne's aneurysm data:
path_to_aneurysm_data = "localhost:/Users/moonshine/CIS_410/finalproject/scientific_visualization/aneurysm_data/"


def SetUpVPV():
    RestoreSession("vpandv.session",0)
    OpenDatabase(path_to_aneurysm_data + "aneurysm*.silo database", 0)
    AddPlot("Volume", "pressure", 1, 1)
    AddPlot("Contour", "velocity_magnitude", 1, 1)
    DrawPlots()

def AnimateInTime():
    for i in range(150):
        TimeSliderSetState(i)
        SaveWindow()

# SetUpVPV()
# AnimateInTime()
# sys.exit()
def main():
    SetUpVPV()
    AnimateInTime()
    sys.exit()