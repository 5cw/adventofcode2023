import getinput, math
inp = getinput.fetch()
line_len = inp.find('\n') + 1
mx = 0
for (sd, startings) in [(line_len, range(-line_len, -1)),
                        (-line_len, range(len(inp) + 1, len(inp) + line_len)),
                        (1, range(-1, len(inp), line_len)),
                        (-1, range(line_len - 1, len(inp), line_len))]:
    for sp in startings:
        beams = [(sp, sd)]
        energized = [set() for _ in range(len(inp))]
        while len(beams) > 0:
            new_beams = []
            for pos, d in beams:
                new = pos + d
                if new < 0 or new >= len(inp) or inp[new] == '\n' or d in energized[new]:
                    continue
                char = inp[new]
                energized[new].add(d)
                if char in '\\/':
                    new_beams.append((new, (1, line_len)[abs(d) == 1]*(1, -1)[d < 0]*(1, -1)[char == '/']))
                elif char in '-|':
                    if abs(d) == line_len and char == '-': new_beams.extend([(new, 1), (new,  -1)])
                    elif abs(d) == 1 and char == '|': new_beams.extend([(new, line_len), (new, -line_len)])
                    else: new_beams.append((new, d))
                else:
                    new_beams.append((new, d))
            beams = new_beams
        mx = max(mx, sum(1 for s in energized if s))
print(mx)