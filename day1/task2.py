with open('elf.txt', 'r') as f:
    data = f.read()

elf_calories = sorted(
    [
        sum(int(e) for e in elf.split('\n'))
        for elf in data.split('\n\n')
    ],
    reverse=True
)

print(sum(elf_calories[:3]))
