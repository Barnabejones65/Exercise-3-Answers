#8
import arcpy
arcpy.env.workspace = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb'
featureClass = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb\CallsforService'
result = arcpy.GetCount_management(featureClass)
print(' {} has {} records'. format(featureClass, result[0]))