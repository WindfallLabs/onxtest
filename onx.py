# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 09:15:24 2017

@author: bt
"""

import arcpy

featureClass = "C:\\z_Workspace\\Python\onxtest\\MissoulaParcelsTest\\MissoulaParcelsTest.shp"
# gets field names from shapefile, assigns to variable
fieldList = arcpy.ListFields(featureClass)
# Loop through each field in the list and print the name
for field in fieldList:
    print field.name
# 
zipcode = "OwnerZip"
cursor = arcpy.SearchCursor(featureClass)
for row in cursor:
    print(row.getValue(zipcode))




"""
row = cursor.next()
while row:
    print(row.getValue(zipcode))
    row = cursor.next
"""