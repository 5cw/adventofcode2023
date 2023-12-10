import re
inp = open('day3input.txt').read()
line_len = inp.find('\n') + 1
total = 0
for n in re.finditer(r'\d+', inp):
    start=n.start()-1
    end=n.end()+1
    surroundings = inp[start - line_len:end - line_len] if end > line_len else ""
    surroundings += inp[start:end] + inp[start + line_len:end + line_len]
    if re.search(r'[^\d.\n]', surroundings) is not None:
        total += int(n[0])
print(total)

total = 0
for m in re.finditer(r'[^\d.\n]', inp):
    s = m.start()
    valid = set()
    for j in range(-1, 2):
        c = s + j*line_len
        valid |= {*range(c - 1,c + 2)}
    adj = []
    for n in re.finditer(r'\d+', inp):
        if {*range(n.start(),n.end())} & valid:
            adj.append(int(n[0]))
    if len(adj) == 2:
        total += adj[0]*adj[1]

print(total)
