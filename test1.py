from common.hr import Designation
d1=Designation(10,"Carpenter")
d1._validate_values()
js=d1.to_json()
print(js)
print("-"*25)
d2=Designation.from_json(js)
print(d2)
print("Code : ",d2.code)
print("Title : ",d2.title)
print("Exceptions : ",d2.exceptions)
print("Has Exception : ",d2.has_exceptions)