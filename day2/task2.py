STATS = {'A': 1, 'B': 2, 'C': 3}
STEP = {'X': -1, 'Y': 0, 'Z': 1}


def get_round_stats(val1, val2):
	return (
			((STEP[val2] + 1) * 3) +  # win stat
			(STATS[val1] + 1 * STEP[val2]) % 3 +  # increase or decrease 1 step
			(((STATS[val1] + 1 * STEP[val2]) % 3) == 0) * 3  # if step equal to 3
	)


with open('data.txt', 'r') as f:
	data = f.read().split('\n')

print(
	sum(
		get_round_stats(*r.split())
		for index, r in enumerate(data)
	)
)
