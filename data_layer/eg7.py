import datetime
d=datetime.datetime(2020,4,24)
print(d,type(d))
ds=d.strftime("%y-%m-%d")
print(ds,type(ds))
ds=d.strftime("%Y-%m-%d")
print(ds,type(ds))
