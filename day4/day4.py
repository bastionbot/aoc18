import datetime
from statistics import mode
from collections import Counter
log = []
dates = []
datetimes = []
guardtimes = {}
mergedlist = []
slackers = {}
slacker = {}
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
datetimes.sort()

guardlist = { date : {} for i in range(0,60) for date in dates }
currentguard = ""
for date in datetimes:
	if 'Guard #' in sortedlog[date]:
		currentguard = sortedlog[date].split('#')[1].split(' ')[0]
		if currentguard not in guards[date.date()].keys():
			guards[date.date()][currentguard] = []
		if currentguard not in guardlist[date.date()].keys():
			guardlist[date.date()][currentguard] = []
	else:
		if currentguard not in guards[date.date()].keys():
			guards[date.date()][currentguard] = []
			guards[date.date()][currentguard].append(date)
		else:
			guards[date.date()][currentguard].append(date)
		if currentguard not in guardlist[date.date()].keys():
			guardlist[date.date()][currentguard] = []

for date in dates:
	for guard in guards[date]:
		for i in range(0, len(guards[date][guard]), 2):
			try:
				x = guards[date][guard][i] # get start of sleep
				y = guards[date][guard][i+1] # get end of sleep
			except:
				break
			for j in range(int(x.time().minute), int(y.time().minute)):
				guardlist[x.date()][guard].append(j)

for date in guardlist:
	for guard in guardlist[date]:
		if guard not in guardtimes.keys():
			guardtimes[guard] = len(guardlist[date][guard])
		else:
			guardtimes[guard] += len(guardlist[date][guard])
print(guardtimes)
sleepy = max(guardtimes, key=guardtimes.get)
print('Guard #'+ str(sleepy) +' slept a total of ' + str(guardtimes[sleepy])+ ' minutes.')

for date in guardlist:
	if sleepy in guardlist[date].keys():
		mergedlist.extend(guardlist[date][sleepy])
asleep = max(mergedlist, key=mergedlist.count)
print('Sleepy spent minute ' + str(asleep) + ' asleep the most.')
print('Part 1 solution: ' + str(int(asleep)*int(sleepy)))

for date in guardlist:
	for guard in guardlist[date].keys():
		if guard not in slackers.keys():
			slackers[guard] = []
		slackers[guard].extend(guardlist[date][guard])
for guard in slackers:
	if slackers[guard]:
		data = Counter(slackers[guard])
		slacker[guard] = slackers[guard].count(data.most_common(1)[0][0])
lazy = max(slacker, key=slacker.get)
lazyminute = Counter(slackers[lazy]).most_common(1)[0][0]
print('Part 2: Guard #'+ str(lazy) + ', minute '+ str(lazyminute) + '\nSolution: ' + str(int(lazy)*int(lazyminute)))
