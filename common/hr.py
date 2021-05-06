import json
class ValidationException(Exception):
    def __init__(self,message="",exceptions=None):
        self.message=message
        self.exceptions=exceptions
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(json_string):
        new_dict=json.loads(json_string)
        return ValidationException(**new_dict)

class Designation:
    def __init__(self,code=0,title="",exceptions={},has_exceptions=False):
        self.exceptions=exceptions
        self.has_exceptions=has_exceptions
        self.code=code
        self.title=title
        self._validate_values()
    def _validate_values(self):
        if isinstance(self.code,int)==False:
            self.exceptions["code"]=('T',f"Code is of type {type(self.code)},it should be of type {type(10)}")
        if isinstance(self.title,str)==False:
            self.exceptions["title"]=('T',f"Title is of type {type(self.title)},it should be of type {type('A')}")
        if ('code' in self.exceptions)==False and self.code<0:
            self.exceptions["code"]=('V',f"Value of code is {self.code} ,it should be greater than 0")
        if ('title' in self.exceptions)==False:
            lengthOfTitle=len(self.title)
            if lengthOfTitle==0 or lengthOfTitle>35:
                self.exceptions["title"]=('V',f"Length of title is {lengthOfTitle}, it should be gretaer than one or less than or equal to 35")
        if len(self.exceptions)>0: self.has_exceptions=True
    def to_json(self):
        return json.dumps(self.__dict__)
    def from_json(json_string):
        new_dict=json.loads(json_string)
        return Designation(**new_dict)








       