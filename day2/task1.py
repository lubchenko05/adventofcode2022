WIN_STAT = 6
DRAW_STAT = 3

STATS = {
	'A': 1, 'B': 2, 'C': 3,
	'X': 1, 'Y': 2, 'Z': 3
}


def get_round_stats(val1, val2):
	choice_stat = STATS[val2]
	if (STATS[val1], STATS[val2]) in ((1, 2), (2, 3), (3, 1)):
		choice_stat += WIN_STAT
	elif STATS[val1] == STATS[val2]:
		choice_stat += DRAW_STAT
	return choice_stat


with open('data.txt', 'r') as f:
	data = f.read().split('\n')

print(
	sum(
		get_round_stats(*r.split())
		for index, r in enumerate(data)
	)
)
