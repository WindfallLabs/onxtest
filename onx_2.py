# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 16:25:15 2017

@author: b
"""
import arcpy


fc = "C:\\z_Workspace\\Python\onxtest\\MissoulaParcelsTest\\MissoulaParcelsTest.shp"

with arcpy.da.UpdateCursor(fc, ["OwnerZip"]) as cursor:
    for row in cursor:
        if row[0] in ["0", "0.0"]:
            row[0] = ""  # if NULL value desired, use None
            cursor.updateRow(row)
            # print (row)

print "Processing complete"
