#13
#Create a gdb
current_dir = r'D:\My Documents_D\GIS 610 - Coding\Question 13'
fgdb_name = 'Question13.gdb'
arcpy.CreateFileGDB_management(current_dir, fgdb_name)

# Define inputs
question13_gdb = r'D:\My Documents_D\GIS 610 - Coding\Question 13\Question13.gdb'
shapefile1 = r'D:\My Documents_D\GIS 610 - Coding\Question 13\Question 13\tl_2018_04_tract.shp'
shapefile2 = r'D:\My Documents_D\GIS 610 - Coding\Question 13\Question 13\tl_2018_us_county.shp'

# Import the shapefiles
arcpy.FeatureClassToGeodatabase_conversion([shapefile1, shapefile2], question13_gdb)
print('import success')

arcpy.Clip_management(shapefile1, shapefile2, "????", 
                      "D:\My Documents_D\GIS 610 - Coding\Question 13\Question13.gdb\clip01", "#", "#", "NONE", "NO_MAINTAIN_EXTENT")
#I got to this point but was not able how to figure out how to complete the clip management tool
