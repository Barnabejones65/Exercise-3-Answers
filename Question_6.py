#6
import arcpy

arcpy.env.workspace = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb'
inFeatures = 'CallsforService'
fieldname = 'Crime_Explanation'
field_type = 'text'

arcpy.AddField_management(inFeatures,fieldname,"TEXT")

featureClass = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb\CallsforService'
FieldNames = ['CFSType','Crime_Explanation']

with arcpy.da.UpdateCursor(featureClass, FieldNames) as cursor:
	for x in cursor:
		if x[0] == ('Burglary Call'):
			x[1] = 'This is a burglary'
			cursor.updateRow(x)

			print('Row Updated!')