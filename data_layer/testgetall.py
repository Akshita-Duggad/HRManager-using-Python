from hr import HRDLHandler,Designation,DataLayerException
import sys
try:
    designations=HRDLHandler.get_designations()
    for designation in designations: 
        print(f"Code : {designation.code} , Title : {designation.title}")
except DataLayerException as dle:
    print(dle.message)
    print(dle.exceptions)