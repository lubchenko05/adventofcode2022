STATS = {
	'A': 1, 'B': 2, 'C': 3,
	'X': 1, 'Y': 2, 'Z': 3
}


def get_round_stats(val1, val2):
	return (
		(((((STATS[val1] + 1) % 3) + 3 * (STATS[val1] % 2 == 0)) == STATS[val2]) * 6) +  # win
		((STATS[val1] == STATS[val2]) * 3) +  # draw
		STATS[val2]  # lose
	)


with open('data.txt', 'r') as f:
	data = f.read().split('\n')

print(
	sum(get_round_stats(*r.split()) for index, r in enumerate(data))
)

