lines = []
table = []
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
			table[i][j] += 1

for line in table:
	for i in line:
		if i > 1:
			squares += 1
print(squares)
