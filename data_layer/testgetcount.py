from hr import HRDLHandler,Designation,DataLayerException
import sys
try:
    count=HRDLHandler.get_designation_count()
    print(f"Number of designation records : {count}")
except DataLayerException as dle:
    print(dle.message)
    print(dle.exceptions)