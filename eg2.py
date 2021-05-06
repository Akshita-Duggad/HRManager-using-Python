import json
a=10
b=type(a)
print(b)
c=b.__name__
print(c,type(c))
d=b("30")
print(d,type(d))
k="2043"
g=f"{c}({k})"
print(g)
u=eval(g)
print(u,type(u))
# implementing in eg3	