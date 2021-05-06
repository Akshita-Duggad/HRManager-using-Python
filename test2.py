from common.hr import Designation
from network_common.wrappers import Request
d1=Designation(10,"Carpenter")
d1._validate_values()
r1=Request("DesignationManager","add",d1)
str=r1.to_json()
print(str)
print("*"*25)
r2=Request.from_json(str)
print("Manager : ",r2.manager)
print("Action : ",r2.action)
print("JSON String : ",r2.json_string)
print("*"*25)
d2=Designation.from_json(r2.json_string)
print(d2)
print("Code : ",d2.code)
print("Title : ",d2.title)
print("Exceptions : ",d2.exceptions)
print("Has exception : ",d2.has_exceptions)




