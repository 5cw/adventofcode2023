import getinput, re, math

#inp = getinput.fetch()

inp = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

line_len = inp.find('\n') + 1

memoize = {}


def parity(x, y=None):
    if y is None:
        y = x % line_len
        x //= line_len
    return (x + y) & 1


def possibilities(pos, steps):
    searched = set()
    searching = [(pos, steps)]
    while searching:
        # print(searching)
        ps, sr = searching.pop(0)
        sr -= 1
        for i in [1, -1, line_len, -line_len]:
            npos = ps + i
            if npos not in searched and 0 <= npos < len(inp) and inp[npos] not in '#\n':
                if sr > 0:
                    searching.append((npos, sr))
                searched.add(npos)
    cmp = parity(pos) ^ (steps & 1)
    valid = [p for p in searched if parity(p) == cmp]
    print(pos, steps)
    print(''.join(c if i not in valid else '0' for i, c in enumerate(inp)) + '\n')
    return len(valid)


spos = inp.find('S')

print(possibilities(spos, 64))

#p2 = 26501365

p2 = 50

full, fulloff = [len([c for i, c in enumerate(inp) if c in '.S' and parity(i) ^ k == parity(spos)])
                 for k in (0, 1)]
print(full, fulloff)

side = line_len - 1

half_side = line_len // 2 - 1

rem = p2 % side
rem2 = rem + side

rem3 = (p2 - half_side - 1) % side
rem4 = rem3 + side

print(rem, rem2, rem3, rem4)


corners = [[possibilities(pos, r) for pos in [0, line_len - 2, len(inp) - line_len, len(inp) - 2]] for r in (rem, rem2)]
edges = [possibilities(pos, r) for r in (rem3, rem4)
         for pos in [half_side, line_len * half_side, line_len * (half_side + 1) - 2, len(inp) - half_side - 2]]
total = sum(edges)
outside, inside = map(sum, corners)
print(outside, inside)

dist = p2 // side + 1
print(dist)
total += dist * outside + (dist - 1) * inside
for i, n in enumerate((full, fulloff)):
    # each ring of repititions has 4 times the distance from the center
    #        #
    #       # #
    #        #
    #
    #        #
    #       # #
    #      #   #
    #       # #
    #        #
    total += sum(4 * n * j if j else n for j in range(i, dist - 2, 2))
print(total)
