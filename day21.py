import getinput, re, math

inp = getinput.fetch()



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
    theory_valid = [i for i, c in enumerate(inp) if c in '.S' and parity(i) == cmp]
    diff = set(theory_valid) - set(valid)
    print(diff)
    print(pos, steps)
    print(''.join((c if i not in diff else 'X') if i not in valid else '0' for i, c in enumerate(inp)) + '\n')
    return len(valid)


spos = inp.find('S')
print(parity(spos))
#print(possibilities(spos, 64))

p2 = 26501365

#p2 = 50

even, odd = [possibilities(spos, i) for i in (200,201)] # some squares have the right parity but are still unreachable.
side = line_len - 1

half_side = line_len // 2 - 1

rem = (p2 - 1) % side
rem2 = rem + side

rem3 = (p2 - half_side - 1) % side

print(rem, rem2, rem3)


corners = [[possibilities(pos, r) for pos in [0, line_len - 2, len(inp) - line_len, len(inp) - 2]] for r in (rem, rem2)]
edges = [possibilities(pos, rem3)
         for pos in [half_side, line_len * half_side, line_len * (half_side + 1) - 2, len(inp) - half_side - 2]]
total = sum(edges)
outside, inside = map(sum, corners)
print(outside, inside)



#   https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
#    I used this to help me understand but my solution still looks a little different.
#    OEO
#   OI1IO
#   E101E
#   OI1IO
#    OEO
#
dist = p2 // side
print(dist)
total += dist * outside + (dist - 1) * inside
total += (dist - 1) ** 2 * odd + dist ** 2 * even
print(total)
