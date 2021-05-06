from hr import HRDLHandler,Designation,DataLayerException
import sys
try:
    code=int(sys.argv[1])
    HRDLHandler.delete_designation(code)
    print("Designation deleted")
except DataLayerException as dle:
    print(dle.message)
    print(dle.exceptions)