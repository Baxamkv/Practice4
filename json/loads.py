from json import loads

jsn = loads("""{"a":{"b":{"c":1}},"x":[10,20]}""")
print(jsn)