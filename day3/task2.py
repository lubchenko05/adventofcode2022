with open('data.txt', 'r') as f:
	data = f.read().split('\n')

total = 0
groups = [data[i * 3: (i + 1) * 3] for i in range(int(len(data) / 3))]

for g in groups:
	same = set(g[0]) & set(g[1]) & set(g[2])
	for s in same:
		if s.islower():
			total += (ord(s) - 96)
		else:
			total += (ord(s) - 38)

print(total)
