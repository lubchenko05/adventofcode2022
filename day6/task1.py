with open('data.txt', 'r') as f:
	data = f.read()

stack = []

for index, d in enumerate(data):
	try:
		duplicate_index = stack.index(d)
	except ValueError:
		stack.append(d)
	else:
		stack = stack[duplicate_index+1:]
		stack.append(d)
		continue

	if len(stack) >= 4:
		print(index + 1)
		break
