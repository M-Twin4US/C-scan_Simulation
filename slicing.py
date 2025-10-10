#This script is to automatically change the position of slicing box

import Rhino

grass = Rhino.RhinoApp.GetPlugInObject('Grasshopper')

guid = '55a195d8-6e04-4f71-875e-3cd92c9b8eb4'
# The instance GUID can be retrieved by the function included in the Grasshopper script

for i in range(0, 2200, 200):
    grass.SetSliderValue(guid, i)
    grass.RunSolver('void.gh')