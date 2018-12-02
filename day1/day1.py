i,j,k = [],[],[]
with open('input.txt') as f:
	for line in f.readlines():
		i.append(line.strip())
for x in i:
	if x[0] =='+':
		j.append(int(x[1:]))
	else:
		k.append(int(x[1:]))
print(j)
print(k)
print(sum(j) - sum(k))
