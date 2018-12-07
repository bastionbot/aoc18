import string
from iteration_utilities import duplicates
coords = {}
maxx,maxy,l = 0,0,0
size = {}
safesize = 0
with open('input.txt') as f:
	for line in f.readlines():
		x,y = line.split(', ')
		x = int(x)
		y = int(y.strip())
		coords[(x, y, string.ascii_letters[l])] = 0
		l+=1
for x,y,foo in coords.keys():
	if x > maxx:
		maxx = x +1
	if y > maxy:
		maxy = y +1

table = [[{} for i in range(maxx)] for j in range(maxy)]
for x,y,foo in coords.keys():
	table[y][x] = { foo: 0}
	size[foo] = 0

for y in range(len(table)):
	for x in range(len(table[y])):
		mindist = 99999
		owner = ''
		for xk, yk, foo in coords.keys():
			if foo not in table[y][x].keys():
				table[y][x][foo] = abs(xk - x) + abs(yk - y)
		if sum(table[y][x].values()) < 10000:
			safesize += 1		
		for key, value in table[y][x].items():
			if value == 0:
				owner = key
				break
			elif mindist > value:
				mindist = value
				owner = key
				if x == 0 or y == 0 or x == maxx or y == maxy:
					size[key] = -9999999
		smol = min(table[y][x].values())
		if smol in list(duplicates(table[y][x].values())):
			owner = '.'
		table[y][x] = owner
for y in range(len(table)):
	for x in range(len(table[y])):
		if table[y][x] == '.':
			continue
		else:
			size[table[y][x]] += 1
print('Winner is %s: %d\nSafe size: %d' % (max(size, key=size.get),int(size[max(size, key=size.get)]), safesize))
