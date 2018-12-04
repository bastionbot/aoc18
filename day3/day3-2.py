lines = []
table = []
dq = []
x,y,runx,runy,maxx,maxy = 0,0,0,0,0,0
squares = 0
with open('input.txt') as f:
	for line in f.readlines():
		lines.append(line.strip())

for line in lines:
	x = int(line.split(':')[0].split(' ')[2].split(',')[0])
	y = int(line.split(':')[0].split(' ')[2].split(',')[1])
	runx = int(line.split(':')[1].split(' ')[1].split('x')[0])
	runy = int(line.split(':')[1].split(' ')[1].split('x')[1])
	if maxx < x+runx:
		maxx = x+runx
	if maxy < y+runy:
		maxy = y+runy

table = [[0 for i in range(maxx)] for j in range(maxy)]

for line in lines:
	x = int(line.split(':')[0].split(' ')[2].split(',')[0])
	y = int(line.split(':')[0].split(' ')[2].split(',')[1])
	runx = int(line.split(':')[1].split(' ')[1].split('x')[0])
	runy = int(line.split(':')[1].split(' ')[1].split('x')[1])
	for i in range(y,runy+y):
		for j in range(x,runx+x):
			if table[i][j] != 0:
				if table[i][j] not in dq:
					dq.append(table[i][j])
				if line.split(' ')[0] in dq:
					continue
				dq.append(line.split(' ')[0])
			elif table[i][j] == 0:
				table[i][j] = line.split(' ')[0]
for line in lines:
	if line.split(' ')[0] in dq:
		continue
	print("Valid claim! " + line.split(' ')[0])
