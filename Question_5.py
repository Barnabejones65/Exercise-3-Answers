#5
import arcpy
print('Import Successful')
#create GDB
from arcpy import env
env.overwriteOutput = True

#Create a gdb
current_dir = r'D:\My Documents_D\GIS 610 - Coding\Exercise3GDB'
fgdb_name = 'Question5.gdb'
arcpy.CreateFileGDB_management(current_dir, fgdb_name)

#Create Feature Classes
current_workspace = r'D:\My Documents_D\GIS 610 - Coding\Exercise3GDB\Question5.gdb'
geometry_type = "POLYGON"
spatial_reference = arcpy.SpatialReference(102100)
featureClassNamesList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']
arcpy.env.workspace = current_workspace
arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):
	arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)
	print('Feature Class ' + in_fc_name + ' was successfully created.')

createFC = [createFeatureClass(fc) for fc in featureClassNamesList]

print('Finished')