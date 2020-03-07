# /Applications/VisIt.app/Contents/Resources/bin/visit -cli -s initialize.py

def SetUp():
    OpenDatabase(
    "localhost:/Users/alyssakelley/Desktop/CIS_410/410_final_project/scientific_visualization/aneurysm_data/aneurysm_data/aneurysm*.silo database",0)
    AddPlot("Pseudocolor", "mesh_quality/shape_and_size", 1, 1)
    DrawPlots()
   
def main():
	SetUp()
