import getinput, re, math

inp = getinput.fetchlines()

dic = {
    'button': ('', ['broadcaster'])
}

conj = {

}

flip = {

}

for line in inp:
    sym, id, dests = re.match(r'([%&]?)([^\s]+) -> (.+)', line).groups()
    dests = dests.split(', ')
    dic[id] = (sym, dests)
    if sym == '&':
        conj[id] = {}
    elif sym == '%':
        flip[id] = False

for id, (sym, dests) in dic.items():
    for dest in dests:
        if dest in conj:
            conj[dest][id] = False
print(dic)
print(conj)
reps = ['ff', 'bq', 'dz', 'kg']
seqs = {rep: {sd: [] for sd in conj[next(k for k in conj if rep in conj[k])]} for rep in reps}
# print(seqs)
hi = lo = 0

pulses = {id: [] for id in dic.keys()}

for i in range(100000):
    queue = [('button', 'broadcaster', False)]

    while queue:

        fr, to, insig = queue.pop(0)
        if insig:
            hi += 1
        else:
            lo += 1
        if to not in dic:
            continue
        sym, dests = dic[to]
        if sym == '&':
            conj[to][fr] = insig
            outsig = not all(conj[to].values())
        elif sym == '%':
            if not insig:
                flip[to] = not flip[to]
                outsig = flip[to]
            else:
                continue
        else:
            outsig = insig
        if to in reps and outsig:
            for k in seqs[to]:
                seqs[to][k].append(flip[k])
        pulses[to].append(i)
        queue.extend([(to, dest, outsig) for dest in dests])
print(hi * lo)

memoize = {}


def find_cycle(node, output):
    if node == 'broadcaster':
        return [int(not output)]
    if (node, output) in memoize:
        return memoize[(node, output)]
    sources = [id for id, (sym, dests) in dic.items() if node in dests]
    if dic[node][0] == '%':
        cycles = [find_cycle(id, False) for id in sources]


bases = set()
for rep in reps:
    for s in seqs[rep]:
        arr = seqs[rep][s]
        counts = []
        find = True
        while find in arr:
            i = arr.index(find)
            counts.append(i)
            arr = arr[i:]
            find = not find
        print(counts)


def printtree(node, visited=None, indent=0):
    if visited is None:
        visited = set()
    print('    ' * indent + dic[node][0] + node + '*' * (node in visited))
    if node in visited:
        return
    sources = [id for id, (sym, dests) in dic.items() if node in dests]
    for src in sources:
        printtree(src, visited | {node}, indent + 1)


#printtree('gf')

cycle = {}
masks = {}
for id, plses in pulses.items():
    if id in flip:
        # plses = plses[::2]
        deltas = [j - i for i, j in zip(plses, plses[1:])]
        cur = plses[0] + 1
        count = 1
        tallies = []
        for delta in deltas:
            if delta != cur:
                if (count, cur) in tallies:
                    break
                tallies.append((count, cur))
                count = 1
            else:
                count += 1
            cur = delta
        print(id + ':', *[f'{count:5}*{cur:5}' for count, cur in tallies], '...')
        cycle[id] = sum(count * cur for count, cur in tallies)
        mask = 0
        high = 0
        i = 0
        for count, cur in tallies:
            for _ in range(count):
                for _ in range(cur):
                    mask |= high << i
                    i += 1
                high ^= 1
        masks[id] = mask
        # print(id, plses)

for k in conj['gf']:
    p = list(conj[k])[0]
    md = {}
    cycs = [cycle[id] for id in conj[p]]
    msks = [masks[id] for id in conj[p]]
    for c, m in zip(cycs, msks):
        if c in md:
            md[c] &= m
        else:
            md[c] = m
    print(cycs)
    step = max(cycs)
    all_on = (1 << step) - 1
    for i in range(0, 100000, step):
        choice = all_on
        for c, m in zip(cycs, msks):
            offset = i % c
            nm = (m >> offset) | (m << (step - offset))
            choice &= nm
        if choice:
            print(i, choice)
            break
print(math.lcm(3761, 4091, 3767, 4001))