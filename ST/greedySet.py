import os
import pprint
import os.path
cache = {}
memCache = {}
def maxIntersection(i, programs, bestSet, pCodeDict, pCount):
	if (i, tuple(bestSet), tuple(pCount)) in memCache:
		return 0
	if i == len(programs) or len(bestSet) == 0:
		bestSet = tuple(bestSet)
		cache[bestSet] = (pCount if (len(cache[bestSet]) < len(pCount)) else cache[bestSet])   if (bestSet in cache) else pCount
		memCache[(i, bestSet, tuple(pCount))] = True
		return len(bestSet)
	# print(pCount)
	return max(maxIntersection(i + 1, programs, bestSet.intersection(pCodeDict[programs[i]]), pCodeDict, pCount + [programs[i]]), maxIntersection(i + 1, programs, bestSet.intersection(bestSet), pCodeDict, pCount))
	maxIntersection( )
programs = os.listdir('sortedPrograms')
programs.sort(key = lambda x: -len(os.listdir(os.path.join("sortedPrograms", x))))
pCodeDict = {}
bestSet = set()
for program in programs:
	pCodeDict[program] = set()
	for code in os.listdir(os.path.join("sortedPrograms", program)):
		user = code.split("_")[0]
		bestSet.add(code.split("_")[0])
		pCodeDict[program].add(user)
print(maxIntersection(0, programs[:50], bestSet, pCodeDict, []))
for key in cache:
	if len(cache[key]) > 10 and len(key) > 3:
		print(key, cache[key])
		print(len(key), cache[key])
