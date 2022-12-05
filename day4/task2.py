with open('data.txt', 'r') as f:
	data = f.read().split('\n')

total = 0

for d in data:
	pairs = [r.split('-') for r in d.split(',')]
	part1 = set(range(int(pairs[0][0]), int(pairs[0][1]) + 1))
	part2 = set(range(int(pairs[1][0]), int(pairs[1][1]) + 1))

	if part1.intersection(part2):
		total += 1

print(total)
