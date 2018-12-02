lines = {}
twos = 0
threes = 0
myDict = {}
with open('input.txt') as f:
	for line in f.readlines():
		lines.update( {line.strip() : {}} )
		myDict.update( {line.strip() : {}} )

for key in lines.keys():
	for char in key:
		if char in lines[key].keys():
			lines[key][char] += 1
		else:
			lines[key].update({char : 1})

for key in lines.keys():
	myDict[key].update({key:val for key, val in lines[key].items() if val != 1})
print(myDict)
for key in myDict.keys():
	if (2 in myDict[key].values()) and (3 in myDict[key].values()):
		twos += 1
		threes += 1
	elif 2 in myDict[key].values():
		twos += 1
	elif 3 in myDict[key].values():
		threes += 1
print(twos*threes)
