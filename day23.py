import getinput, re, math, dataclasses, sys

sys.setrecursionlimit(100000)

inp = getinput.fetch()
line_len = inp.find('\n') + 1
dirs = [-1, 1, -line_len, line_len]
dists = [None if c in '#\n' else 0 for c in inp]

searching = [(0, 1)]

while searching:
    fr, pos = searching.pop(0)
    for dr in {'.': dirs, 'v': [line_len], '>': [1]}[inp[pos]]:
        npos = pos + dr
        if npos < 0 or npos > len(inp) or dists[npos] is None or fr == npos:
            continue
        dists[npos] = max(dists[npos], dists[pos] + 1)
        searching.append((pos, npos))

print(dists[-3])

nodes = [1, len(inp) - 3]
nodes += [pos for pos in range(len(inp))
          if inp[pos] not in '\n#' and
          sum(0 < pos + dr < len(inp) and inp[pos + dr] not in '\n#' for dr in dirs) > 2]
connections = {}


def cnx(pos, fr=None):
    if pos in nodes and fr:
        return {(pos, 0)}
    out = set()
    if not (0 < pos < len(inp)) or inp[pos] in '\n#':
        return out
    for dr in dirs:
        if pos + dr != fr:
            out |= cnx(pos + dr, pos)
    return {(p, ct + 1) for p, ct in out}

for pos in nodes:
    connections[pos] = cnx(pos)

searching = [([1], 0)]
l = 0
while searching:
    visited, dist = searching.pop()
    if visited[-1] == 20019:
        l = max(dist, l)
        continue
    print(len(searching))
    for cpos, cdist in connections[visited[-1]]:
        if cpos not in visited:
            searching.append((visited + [cpos], dist + cdist))
print(l)