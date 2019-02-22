#9
import arcpy

#Create Feature Classes
current_workspace = r'D:\My Documents_D\GIS 610 - Coding\Exercise3GDB\Question5.gdb'
geometry_type = "POLYGON"
spatial_reference = arcpy.SpatialReference(102100)
featureClassNamesList = ['Highways']
arcpy.env.workspace = current_workspace
arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):
	arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)
	print('Feature Class ' + in_fc_name + ' was sucessfully created.')

createFC = [createFeatureClass(fc) for fc in featureClassNamesList]

print('FC Created!')

#Create Field
inFeatures = 'Highways'
fieldname = 'NewSelection'
field_type = 'text'

arcpy.AddField_management(inFeatures, fieldname, "TEXT")

featureClass = r'D:\My Documents_D\GIS 610 - Coding\Exercise3GDB\Question5.gdb\Highways'

print('Field Created!')

#Add Domains
# Set local parameters
domName = "NewDomain"
gdb = current_workspace
inFeatures = featureClass
inField = fieldname
 
# Create the coded value domain
arcpy.CreateDomain_management(gdb, domName, "Highways", 
                              "TEXT", "CODED")
    
# Store all the domain values in dictionary with the domain code as the "key" 
# Domain description = "value" (domDict[code])
domDict = {"1":"I17", "2": "I10", "3": "51", 
           "4": "101", "5": "303"}

# Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
    
# Constrain the material value of distribution mains
arcpy.AssignDomainToField_management(inFeatures, inField, domName)

print('Hit the Road!')