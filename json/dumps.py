from json import dumps

jsn = {"b" : 3, "c" : 7}
print(dumps(jsn,indent=3,sort_keys=True))