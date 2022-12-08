from functools import reduce

grid = [[int(i) for i in line] for line in open('data.txt', 'r').read().split("\n")]


def get_view_range(grid, x, y, direction=1, axis='x'):
	if axis == 'x':
		line = grid[y][x+1:] if direction == 1 else grid[y][:x][::-1]
	else:
		line = [c[x] for c in grid[y+1:]] if direction == 1 else [c[x] for c in grid[:y]][::-1]

	cur_view = 0

	for i in line:
		cur_view += 1
		if i >= grid[y][x]:
			break

	return cur_view


highest_view = max(
	reduce(lambda x, y: x*y, (
		get_view_range(grid, r, c, direction=1, axis='x'),
		get_view_range(grid, r, c, direction=-1, axis='x'),
		get_view_range(grid, r, c, direction=1, axis='y'),
		get_view_range(grid, r, c, direction=-1, axis='y')
	))
	for r in range(len(grid))
	for c in range(len(grid[r]))
)

print(highest_view)
