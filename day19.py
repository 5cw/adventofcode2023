import getinput, re, math, copy

inp = getinput.fetchlines()
delim = inp.index('')
workflows, parts = inp[:delim], inp[delim+1:]

workflows = {m[1]: m[2].split(',') for m in [re.search(r'(.+)\{(.+)}', workflow) for workflow in workflows]}
#print(workflows)
parts = [{s[0]: int(s[2:]) for s in part[1:-1].split(',')} for part in parts]

total = 0

for part in parts:
    wfi = 'in'
    while wfi not in 'RA':
        workflow = workflows[wfi]
        for wf in workflow:
            #print(wf)
            match = re.match(r'([xmas])([<>])(\d+):(.+)', wf)
            if match:
                v, s, n, d = match.groups()
                if s == '<' and part[v] < int(n) or s == '>' and part[v] > int(n):
                    wfi = d
                    break
            else:
                wfi = wf
        if wfi == 'A':
            total += sum(part.values())

print(total)

searching = [('in', {l: [1, 4000] for l in 'xmas'})]
total = 0
while searching:
    new_searching = []
    for wfi, part in searching:
        if wfi in 'RA':
            if wfi == 'A':
                total += math.prod(x2 - x1 + 1 for x1, x2 in part.values())
            continue
        workflow = workflows[wfi]
        for wf in workflow:
            match = re.match(r'([xmas])([<>])(\d+):(.+)', wf)
            if match:
                v, s, n, d = match.groups()
                n = int(n)
                if s == '<':
                    if part[v][1] < n:
                        new_searching.append((d, part))
                        break
                    elif part[v][0] <= n:
                        d1 = copy.deepcopy(part)
                        d1[v][1] = n - 1
                        part[v][0] = n
                        new_searching.append((d, d1))
                else:
                    if part[v][0] > n:
                        new_searching.append((d, part))
                        break
                    elif part[v][1] >= n:
                        d1 = copy.deepcopy(part)
                        d1[v][0] = n + 1
                        part[v][1] = n
                        new_searching.append((d, d1))
            else:
                new_searching.append((wf, part))

    searching = new_searching
    print(searching)
print(total)