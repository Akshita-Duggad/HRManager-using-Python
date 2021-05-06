from hr import HRDLHandler,Designation,DataLayerException
import sys
try:
    code=int(sys.argv[1])
    designation=HRDLHandler.get_designation_by_code(code)
    print(f"Code : {designation.code} , Title : {designation.title} ")
except DataLayerException as dle:
    print(dle.message)
    print(dle.exceptions)