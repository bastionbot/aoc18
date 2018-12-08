#!/bin/python3
import string, sys
global step 
step = ''
reqs = {}
steps = []
presteps = []
workers = []
with open(sys.argv[1]) as f:
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

def valid_step(reqs):
	foo = None
	for k in sorted([j for j,v in reqs.items() if not v]):
		try:
			if k not in step and k == min(list(set(''.join([j for j,v in reqs.items() if not v])) - set(step))):
				foo = k
		except:
			continue
	return foo
def remove_step(reqs, k):
	global step
	for l in reqs.keys():
		try:
			reqs[l].remove(k)
		except:
			continue
	step += k
	return reqs, step
class worker:
	def __init__(self):
		self.status = 'Idle'
		self.starttime = 0
		self.step = '.'
timer = 0
for i in range(int(sys.argv[2])):
	workers.append(worker())
info = ("Second", '\t'.join(['Elf'+str(i) for i in range(int(sys.argv[2]))]), "Step")
while (len(step) < len(steps)+1):
	for worker in workers:
		if worker.status == 'Working':
			if worker.step is not None:
				if (string.ascii_uppercase.index(worker.step) + 1) + worker.starttime == timer:
					worker.status = 'Idle'
					worker.starttime = 0
					reqs, step = remove_step(reqs, worker.step)
					worker.step = '.'
		elif worker.status == 'Idle' and valid_step(reqs) not in [work.step for work in workers] and valid_step(reqs) is not None:
			worker.step = valid_step(reqs)
			worker.status = 'Working'
			worker.starttime = timer
		else:
			worker.status = 'Idle'
	if valid_step(reqs) not in [work.step for work in workers] and valid_step(reqs) is not None:
		continue
	timer += 1
	print('%s\t%s\t%s' % info)
	info = (str(timer), '\t'.join([worker.step for worker in workers]), step)
print("Total time: %d\nFinal step: %s" % (timer, ''.join(step)))
