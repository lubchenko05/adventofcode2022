data = open('data.txt', 'r').read().split("\n$ ")[1:]
root_dirs, current_path, sizes, ls_buffer = set(), [], {}, []

for command in data:
	c_in = command.split('\n')[0]
	c_out = command.split('\n')[1:]

	if c_in.startswith('cd'):
		if c_in[3:] == '..':
			current_path.pop()

		else:
			current_path.append(c_in[3:])

	if c_in.startswith('ls'):
		cur_size = sum(int(line.split()[0]) for line in c_out if not line.startswith('dir'))
		sizes['/'.join(current_path) if current_path else 'root'] = cur_size

		for i in range(len(current_path)):
			sizes['/'.join(current_path[:i]) if current_path[:i] else 'root'] += cur_size

sizes['root'] += sum(sizes[d] for d in root_dirs)

valid_sizes = list(sorted(
	((k, v) for k, v in sizes.items() if v >= (sizes['root'] - 40_000_000)),
	key=lambda x: x[1]
))

print(valid_sizes[0])