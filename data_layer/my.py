class Designation:
    def __init__(self,code,title):
        self.has_exceptions=False
        self.exceptions=dict()
        self.code=code
        self.title=title
        self._validate_values()
    def _validate_values(self):
        if isinstance(self.code,int)==False:
            self.exceptions["code"]=("T",f"type of code is {type(self.code)} , it should be {type(10)}")
        if isinstance(self.title,str)==False:
            self.exceptions["title"]=("T",f"type of title is {type(self.title)} , it should be {type('A')}")
        if ("code" in self.exceptions)==False and self.code<0:
            self.exceptions["code"]=("V",f"value of code is {self.code} it should be greater than or equal to 0")
        if ("title" in self.exceptions)==False:
            lengthOfTitle=len(self.title)
            if lengthOfTitle==0 or lengthOfTitle>35:
                self.exceptions["title"]=("V",f"length of title is {lengthOfTitle} it should be greater than 0 or less than 35")
        if len(self.exceptions)>0: self.has_exceptions=True


