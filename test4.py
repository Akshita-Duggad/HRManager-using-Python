from common.hr import Designation
from network_common.wrappers import Request,Wrapper
r1=Request("DesignationManager","getDesignationByCode",Wrapper(10))
str=r1.to_json()
print(str)
print("*"*25)
r2=Request.from_json(str)
print("Manager : ",r2.manager)
print("Action : ",r2.action)
print("JSON String : ",r2.json_string)
print("*"*25)
value=Wrapper.from_json(r2.json_string)
print(value,type(value))
