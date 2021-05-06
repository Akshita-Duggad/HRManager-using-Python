# if we are passing int as request_object then it will call to_json or from_json
#which will raise error int and other primitives are json serializable
# they dont need other methods
# solution in eg2

import json
a="good"
j=json.dumps(a)
print(j)
a=10
j=json.dumps(a)
print(j)
