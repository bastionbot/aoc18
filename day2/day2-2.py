lines = []

with open('input.txt') as f:
	for line in f.readlines():
		lines.append(line.strip())

for line in lines:
	for linetwo in lines:
		count_diffs = 0
		for a,b in zip(line, linetwo):
			if a!=b:
				count_diffs +=1
		if count_diffs == 1:
			print(line, linetwo, count_diffs)
