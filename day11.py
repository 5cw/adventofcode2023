import itertools, getinput

inp = getinput.fetchlines()
rows = [i for i in range(len(inp)) if '#' not in inp[i]]
cols = [i for i in range(len(inp[0])) if '#' not in [line[i] for line in inp]]
for factor in [2, 1000000]:
    galaxies = []
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '#':
                y = i + len([row for row in rows if row < i])*(factor - 1)
                x = j + len([col for col in cols if col < j])*(factor - 1)
                galaxies += [(x, y)]

    total = 0
    for ((x1, y1), (x2, y2)) in itertools.combinations(galaxies, 2):
        total += abs(x2 - x1) + abs(y2 - y1)
    print(total)