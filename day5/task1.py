import re

with open('data.txt', 'r') as f:
	data = f.read().split('\n\n')


def get_by_index(state, x, y):
	try:
		return state[x][y] if state[x][y] != '-' else None
	except IndexError:
		return


state = [
	line
	.replace('    ', ' - ')
	.replace('[', '')
	.replace(']', '')
	.split()
	for line in data[0].split('\n')[:-1]
]

state_max_len_range = range(max(len(l_) for l_ in state) + 1)
format_state = []
for l in state_max_len_range:
	line = []
	for r in state_max_len_range:
		item = get_by_index(state, r, l)
		if item:
			line.append(item)
	format_state.append(line)

movements = [
	[int(d) for d in re.findall(r'\d+', line)]
	for line in data[1].split('\n')
]

for m in movements:
	to_move = [l for l in format_state[m[1]-1][:m[0]]][::-1]
	del format_state[m[1]-1][:m[0]]
	format_state[m[2]-1] = to_move + format_state[m[2]-1]

print(''.join(l[0] for l in format_state if len(l)))
