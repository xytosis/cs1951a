import glob,os
import json

jsonobjects = {}

os.chdir("../data")
for f in glob.glob("*.json"):
	with open(f) as jsonfile:
		name = f.split(".")[0]
		print name
		a = json.load(jsonfile)
		jsonobjects[name] = a

with open("all.json", "wb") as output:
	json.dump(jsonobjects, output)
