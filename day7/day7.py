step = ''
reqs = {}
steps = []
presteps = []
with open('input.txt') as f:
	for line in f.readlines():
		p = line.strip().split(' ')[7]
		s = line.strip().split(' ')[1]
		if p not in presteps:
			presteps.append(p)
		if s not in steps:
			steps.append(s)
		if p not in reqs.keys():
			reqs[p] = [s]
		else:
			reqs[p].append(s)
for k in sorted(reqs, key=lambda k: len(reqs[k]), reverse=True):
	print(k, reqs[k])
step = ''.join(sorted(list(set(steps) - set(presteps))))
while (len(step) < len(steps)+1):
	for k, v in sorted(reqs.items()):
		reqs[k] = list(set(reqs[k]) - set(step))
		if len(reqs[k]) == 0 and k not in step:
			step += k
print(''.join(step))
