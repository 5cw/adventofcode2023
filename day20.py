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
#print(dic)
#print(conj)
hi = lo = 0

pulses = {id: [] for id in dic.keys()}

for i in range(10000):
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
        pulses[to].append(i)
        queue.extend([(to, dest, outsig) for dest in dests])
print(hi * lo)



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
        #print(id + ':', *[f'{count:5}*{cur:5}' for count, cur in tallies], '...')
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

cyc_lens = []
for k in conj['gf']:
    p = list(conj[k])[0]
    md = {}
    cycs = [cycle[id] for id in conj[p]]
    cyc_lens.append(cycs.pop())

print(math.lcm(*cyc_lens))