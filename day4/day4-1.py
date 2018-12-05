import datetime
from statistics import mode
log = []
dates = []
datetimes = []
guardtimes = {}
mergedlist = []
guards = {} # logs all guards and when they sleep

with open('input.txt') as f:
	for line in f.readlines():
		log.append(line.strip())

sortedlog = { datetime.datetime.strptime(ts.split(']')[0].split('[')[1], '%Y-%m-%d %H:%M'): ts.split(']')[1].strip() for ts in log }
for date in list(sortedlog.keys()):
	dates.append(date.date())
	datetimes.append(date)
	guards[date.date()] = {}
dates = sorted(set(dates))
datetimes = sorted(datetimes)

guardlist = { date : {} for i in range(0,60) for date in dates }

for date in datetimes:
	if 'Guard #' in sortedlog[date]:
		currentguard = sortedlog[date].split('#')[1].split(' ')[0]
		guards[date.date()][currentguard] = []
		guardlist[date.date()][currentguard] = []
	else:
		if currentguard not in guards[date.date()].keys():
			guards[date.date()][currentguard] = []
		guards[date.date()][currentguard].append(date)
		guardlist[date.date()][currentguard] = []

for date in guards:
	for guard in guards[date]:
		for i in range(len(guards[date][guard])):
			try:
				x = guards[date][guard][i] # get start of sleep
				y = guards[date][guard][i+1] # get end of sleep
			except:
				break
			guard_time, remainder = divmod((y-x).total_seconds(), 60)
			i+=1
			for i in range(x.time().minute, y.time().minute):
				guardlist[x.date()][guard].append(i)

for date in dates:
	total = 0
	for guard in guardlist[date]:
		if guard not in guardtimes.keys():
			guardtimes[guard] = 0
		total += len(guardlist[date][guard])
		guardtimes[guard] += total
sleepy = max(guardtimes, key=guardtimes.get)
print('Guard #'+ str(sleepy) +' slept the most.')
for date in dates:
	if sleepy in guardlist[date].keys():
		mergedlist += guardlist[date][sleepy]
asleep = max(set(mergedlist), key=mergedlist.count)
print('Sleepy spent minute ' + str(asleep) + ' asleep the most.')
print('Solution: ' + str(int(asleep)*int(sleepy)))
