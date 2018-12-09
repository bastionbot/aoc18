#!/bin/python3
import string, sys
global step 
global reqs
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
	available_steps = [j for j,v in reqs.items() if not v]
	k = sorted(list(set([j for j,v in reqs.items() if not v]) - set(step)))
	return k

def remove_step(k):
	global step
	global reqs
	for l in reqs.keys():
		try:
			reqs[l].remove(k)
		except:
			continue
	step += k
class worker:
	def __init__(self, elf):
		self.status = 'Idle'
		self.starttime = 0
		self.step = '.'
		self.elf = elf
timer = 0
for i in range(int(sys.argv[2])):
	workers.append(worker(i))
info = ("Second", '\t'.join(['Elf'+str(i) for i in range(int(sys.argv[2]))]), "Done")
while (len(step) < len(steps)+1):
	current_steps = list(set(valid_step(reqs)) - set([worker.step for worker in workers]))
	if '.' in current_steps:
		current_steps.remove('.')
	for worker in workers:
		if worker.status != 'Working' and current_steps:
			worker.step = min(current_steps)
			current_steps.remove(worker.step)
			worker.status = 'Working'
			worker.starttime = timer
		if worker.status == 'Working' and (string.ascii_uppercase.index(worker.step) + 61) + worker.starttime == timer:
			remove_step(worker.step)
			current_steps = list(set(valid_step(reqs)) - set([worker.step for worker in workers]))
			if '.' in current_steps:
				current_steps.remove('.')
			try:
				worker.step = min(current_steps)
				current_steps.remove(worker.step)
				worker.status = 'Working'
				worker.starttime = timer
			except:
				worker.status = 'Idle'
				worker.step = '.'
	print('%s\t%s\t%s' % info)
	timer += 1
	info = (str(timer), '\t'.join([worker.step for worker in workers]), step)
print('%s\t%s\t%s' % (str(timer), '\t'.join([worker.step for worker in workers]), step))
