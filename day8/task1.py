grid = [[int(i) for i in line] for line in open('data.txt', 'r').read().split("\n")]
total_visible = len(grid) * 2 + (len(grid[0]) - 2) * 2

for r in range(1, len(grid) - 1):
	for c in range(1, len(grid[r]) - 1):
		if any((
			all(grid[r][c] > grid[x][c] for x in range(0, r)),
			all(grid[r][c] > grid[x][c] for x in range(r+1, len(grid))),
			all(grid[r][c] > grid[r][y] for y in range(0, c)),
			all(grid[r][c] > grid[r][y] for y in range(c+1, len(grid[r]))),
		)):
			total_visible += 1

print(total_visible)
