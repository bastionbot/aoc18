import datetime, itertools
log = []
guards = {}
with open('input.txt') as f:
	for line in f.readlines():
		log.append(line.strip())

sortedlog = { datetime.datetime.strptime(ts.split(']')[0].split('[')[1], '%Y-%m-%d %H:%M'): ts.split(']')[1].strip() for ts in log }
guardlist = { date.date() : {} for i in range(0,60) for date in list(set(sortedlog.keys()))}

for item in sorted(sortedlog.keys()):
	print(item)
	if "Guard #" in sortedlog[item]:
		guards[sortedlog[item].split('#')[1].split(' ')[0]] = []
		currentguard = sortedlog[item].split('#')[1].split(' ')[0]
	else:
		guards[currentguard].append(item)
for guard in guards:
	for i in range(len(guards[guard])):
		try:
			foo = guards[guard][i+1]
			x = guards[guard][i]
			y = guards[guard][i+1]
			guardlist[x.date()][guard] = []
		except:
			break
		guard_time, remainder = divmod((y-x).total_seconds(), 60)
		for i in range(x.time().minute, y.time().minute):
			guardlist[x.date()][guard].append(i)

for date in guardlist:
	for guard in guardlist[date]:
		print(guard, len(guardlist[date][guard]))

for guard in guards:
	for date in guardlist.keys():
		try:
			print(date, guard, guardlist[date][guard])
		except:
			continue
