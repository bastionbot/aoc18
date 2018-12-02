import itertools
i = 0
lines,j = [],[]
with open('input.txt') as f:
	for line in f.readlines():
		lines.append(line)

for line in itertools.cycle(lines):
	if line[0] == '+':
		i = i + int(line[1:])
	else:
		i = i - int(line[1:])
	if i in j:
		break
	j.append(i)
	print(i, len(j))
print(i)
