from collections import defaultdict
import copy


import getinput, re
import random


inp = getinput.fetchlines()

matrix = defaultdict(list)
edgelist = []
for line in inp:
    wire1, wires = line.split(': ')
    for wire2 in wires.split():
        matrix[wire1].append(wire2)
        matrix[wire2].append(wire1)
        if {wire1, wire2} not in edgelist:
            edgelist.append({wire1, wire2})

mx = 100
cpy = {}
sizes = {}
# sloppy implementation of Karger's Algorithm based on https://github.com/cshjin/MinCutAlgo/blob/master/algo/MinCut.py
while mx > 3:
    cpy = copy.deepcopy(matrix)
    sizes = {k:1 for k in cpy.keys()}
    while len(cpy) > 2:

        s = random.choice(list(cpy.keys()))
        t = random.choice(cpy[s])
        cpy[s].extend([e for e in cpy[t] if e != s])
        for e in cpy[t]:
            cpy[e].remove(t)
            if e != s:
                cpy[e].append(s)
        sizes[s] += sizes[t]
        del sizes[t]
        del cpy[t]
    mx = min(len(cpy[list(cpy.keys())[0]]), mx)
    print(cpy, sizes, mx)

total = 1
for k in cpy.keys():
    print(k, sizes[k])
    total *= sizes[k]
print(total)
