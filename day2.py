import re
inp = open('day2input.txt').readlines()
total = 0
maxes = {'red': 12, 'green': 13, 'blue': 14}
for i, line in enumerate(inp):
    line = re.split(r'[,;]', line.split(":")[1])
    for pair in line:
        n, c = pair.split()
        if int(n)>maxes[c]:
            break
    else:
        total += i + 1
print(total)

total = 0
for line in inp:
    ns = {}
    line = re.split(r'[,;]', line.split(":")[1])
    for pair in line:
        n, c = pair.split()
        ns[c] = max(ns.get(c, 0), int(n))
    total += ns['red'] * ns['blue'] * ns['green']

print(total)