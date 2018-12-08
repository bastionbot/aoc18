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
for char in ''.join(sorted(list(set(steps) - set(presteps)))):
	reqs[char] = []
while (len(step) < len(steps)+1):
	for k in sorted([j for j,v in reqs.items() if not v]):
		try:
			if k not in step and k == min(list(set(''.join([j for j,v in reqs.items() if not v])) - set(step))):
				step += k
				for l in reqs.keys():
					try:
						reqs[l].remove(k)
					except:
						continue
		except:
			continue
print(''.join(step))
