# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 16:25:15 2017

@author: b
"""
import arcpy


fc = "C:\\z_Workspace\\Python\onxtest\\MissoulaParcelsTest\\MissoulaParcelsTest.shp"

"""
with arcpy.da.UpdateCursor(fc, ["OwnerZip"]) as cursor:
    for row in cursor:
        if row[0] in ("0" or "0.0"):
            row[0] = ""
            cursor.updateRow(row)
            # print (row)
"""
rows = arcpy.UpdateCursor(fc)
for row in rows:
    if row.OwnerZip in ("0" or "0.0"):
        row.OwnerZip = ""
        rows.updateRow(row)

print "Processing complete"