with open('data.txt', 'r') as f:
	data = f.read().split('\n')

total = 0

for line in data:
	part_width = int(len(line) / 2)
	same = set(line[:part_width]).intersection(set(line[part_width:]))
	for s in same:
		if s.islower():
			total += (ord(s) - 96)
		else:
			total += (ord(s) - 38)

print(total)
