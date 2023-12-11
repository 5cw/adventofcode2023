inst, _, *inp = open('day8input.txt').readlines()
inst = inst[:-1]
lookup = {line[:3]: (line[7:10], line[12:15]) for line in inp}
current = 'AAA'
i = 0
while current != 'ZZZ':
    dir = inst[i % len(inst)] == "R"
    current = lookup[current][dir]
    i += 1

print(i)

currents = [key for key in lookup.keys() if key[2] == 'A']
i = 0
zs = {i: [] for i in range(len(currents))}
while i<100000:
    dir = inst[i % len(inst)] == "R"
    currents = [lookup[cur][dir] for cur in currents]
    for n, cur in enumerate(currents):
        if cur[2] == 'Z':zs[n].append(i)
    i += 1
import math
mul = 1
for key in zs:
    mul = math.lcm(mul, zs[key][0] - zs[key][1])

print(mul)