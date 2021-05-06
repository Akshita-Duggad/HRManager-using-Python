from hr import DBConfiguration
#d=DBConfiguration(10,"sdf",40,50,444)
d=DBConfiguration("localhost",34567898765,"hrdb","hr","hr")
print(d.has_exceptions)
print(d.exceptions)