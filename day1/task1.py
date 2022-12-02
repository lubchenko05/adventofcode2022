with open('elf.txt', 'r') as f:
    data = f.read()

print(max(sum(int(e) for e in elf.split('\n')) for elf in data.split('\n\n')))
