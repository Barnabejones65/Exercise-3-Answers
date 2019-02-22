#10
import arcpy

arcpy.env.workspace = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb'

target_features = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb\Tracts'
join_features = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb\General_Offense'
out_feature_class = r'D:\My Documents_D\GIS 610 - Coding\Exercise 3.gdb\Tracts_General_Offense'

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)
print('SJoin Complete!')