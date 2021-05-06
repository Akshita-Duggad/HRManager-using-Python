from hr import HRDLHandler,Designation,DataLayerException
import sys
try:
    title=sys.argv[1]
    designation=HRDLHandler.get_designation_by_title(title)
    print(f"Code : {designation.code} , Title : {designation.title} ")
except DataLayerException as dle:
    print(dle.message)
    print(dle.exceptions)