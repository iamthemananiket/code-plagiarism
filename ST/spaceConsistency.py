import os
import re
import os.path
for pName in os.listdir("sortedPrograms"):
	for program in os.listdir(os.path.join("sortedPrograms", pName)):
		f = open(os.path.join(os.path.join("sortedPrograms", pName), program), "r")
		for content in f.readlines():
			print([ x for x in re.findall("\s+", content.strip())])
		f.close()