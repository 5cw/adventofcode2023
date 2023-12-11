inp = open('day10input.txt').read()
line_len = inp.find('\n') + 1
explored = set()
exploring = [(inp.find('S'), 'L')]
i = 0
connections = {
    '|': (-line_len, line_len),
    '-': (-1, 1),
    'L': (-line_len, 1),
    'J': (-line_len, -1),
    '7': (line_len, -1),
    'F': (line_len, 1)
}
while exploring:
    i += 1
    nextploring = []
    for coord, char in exploring:
        for j in connections[char]:
            if coord + j not in explored:
                nextploring.append((coord + j, inp[coord + j]))
        explored.add(coord)
    exploring = nextploring
print(i - 1)

orthogonal = {
    '|': ([-1], [1]),
    '-': ([line_len], [-line_len]),
    'L': ([-1, line_len - 1, line_len], [-line_len + 1]),
    'J': ([-line_len - 1], [line_len, line_len + 1, 1]),
    '7': ([-line_len, -line_len + 1, 1],[ line_len - 1]),
    'F': ([line_len + 1], [-line_len, -line_len - 1, -1])
}

inside = set()
insploring = set()
end = last = inp.find('S')
current = last + 1
while current != end:
    char = inp[current]
    for j in range(2):
        delta = connections[char][j]
        if delta + current != last:
            for left in orthogonal[char][j]:
                if left + current not in explored:
                    insploring.add(left + current)
            last = current
            current = delta + current
            break
    #print(current, last)

while insploring:
    nextploring = set()
    for i in insploring:
        for d in [-1,1,-line_len,line_len]:
            if i+d not in (insploring | nextploring | inside | explored):
                nextploring.add(i+d)
    inside |= insploring
    insploring = nextploring
    #print(insploring)


def color(i, c):
    char = [c, '#'][i in inside]
    if i in explored: char = '\33[41m' + char + '\33[0m'
    return char


print(''.join(color(i, c) for i, c in enumerate(inp.translate(str.maketrans('|-JL7F', '│─┘└┐┌')))))

print(len(inside))