import json

class Our_json(object):
	pass

myJason = Our_json()
myJason.content = {}
myJason.content["login"] = "Adam_Harkoman"
myJason.content["password"] = "69"

f = open("database.txt", "a")

json.dump(myJason.content, f)
f.close()
f = open("database2.txt", "r")
jObj = json.load(f)
print(jObj['login'])
f.close()