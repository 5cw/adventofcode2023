import getinput


def shift(line):
    sp = line.split('#')
    return '#'.join(('O'*piece.count('O')).rjust(len(piece), '.') for piece in sp)


def cycle(rocks):
    for dir in ['north', 'west', 'south', 'east']:
        rocks = [shift(''.join(line[i] for line in rocks[::-1])) for i in range(len(rocks[0]))]
        print(dir)
        for line in rocks:
            print(line)
        print()
    return rocks

inp = getinput.fetchlines()
seen = [inp]
rocks = cycle(inp)
while rocks not in seen:
    seen.append(rocks)
    rocks = cycle(rocks)


cycstart = seen.index(rocks)
cyclen = len(seen) - cycstart
print(cycstart, cyclen)
loops = 1_000_000_000
end = seen[cycstart + ((loops - cycstart) % cyclen)]

w = [len(inp) + 1] * len(inp[0])
total = 0
for i, line in enumerate(inp):
    for j, c in enumerate(line):
        if c == "#":
            w[j] = len(inp) - i
        elif c == 'O':
            w[j] -= 1
            total += w[j]
    print(line, w)
print(total)

total = 0
for i, line in enumerate(end):
    for j, c in enumerate(line):
        if c == 'O':
            total += len(end) - i
print(total)