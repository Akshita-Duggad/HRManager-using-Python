from common.hr import Designation
from network_common.wrappers import Response
d1=Designation(10,"Carpenter")
d1._validate_values()
r1=Response(True,result_object=d1)
str=r1.to_json()
print(str)
print("*"*25)
r2=Response.from_json(str)
print("Success : ",r2.success)
print("Error : ",r2.error_json_string)
print("Result : ",r2.result_json_string)
print("*"*25)
d2=Designation.from_json(r2.result_json_string)
print(d2)
print("Code : ",d2.code)
print("Title : ",d2.title)
print("Exceptions : ",d2.exceptions)
print("Has exception : ",d2.has_exceptions)




