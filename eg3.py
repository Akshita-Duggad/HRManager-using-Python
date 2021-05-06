import json
class Wrapper:
    def __init__(self,value):
        self.value=value
        self.class_name=type(value).__name__
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(json_string):
        new_dict=json.loads(json_string)
        value=new_dict["value"]
        class_name=new_dict["class_name"]
        return eval(f"{class_name}({value})")

w=Wrapper(10)
j=w.to_json()
print(j)
value=Wrapper.from_json(j)
print(value,type(value))
print("*"*25)

w=Wrapper(10.34)
j=w.to_json()
print(j)
value=Wrapper.from_json(j)
print(value,type(value))
print("*"*25)



w=Wrapper(True)
j=w.to_json()
print(j)
value=Wrapper.from_json(j)
print(value,type(value))
print("*"*25)
