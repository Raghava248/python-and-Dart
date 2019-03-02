import json
#Coverting JSON to Python
x = '{"id":456,"company":"Google","project":"Solar"}'
y = json.loads(x)
#The Result is a Python Dictonary
print(y)

#---------------------------------------------------
#Converting Python to JSON
x = {"id":456,"company":"Google","project":"Solar"}
y = json.dumps(x)
#Printin the resultant json
print(y)
