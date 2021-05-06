from hr import HRDLHandler,Designation,DataLayerException
import sys
try:
    code=int(sys.argv[1])
    title=sys.argv[2]
    designation=Designation(code,title)
    HRDLHandler.update_designation(designation)
    print("Designation updated")
except DataLayerException as dle:
    print(dle.message)
    print(dle.exceptions)