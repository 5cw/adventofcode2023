import getinput

inp = getinput.fetch().split('\n\n')


def find_ref(pattern, avoid = None):
    lines = pattern.strip().split('\n')
    h = len(lines)
    w = len(lines[0])

    for i in range(h - 1):
        if all(l1 == l2 for l1, l2 in zip(lines[i::-1], lines[i + 1:])) and (i + 1) * 100 != avoid:
            return (i + 1) * 100
    for i in range(w - 1):
        if all(all(c1 == c2 for c1, c2 in zip(line[i::-1], line[i + 1:])) for line in lines) and (i + 1) != avoid:
            return (i + 1)
    return None


total = change_total = 0
for pattern in inp:
    val = find_ref(pattern)
    total += val
    for change in range(len(pattern)):
        if pattern[change] not in '.#':
            continue
        newpattern = pattern[:change] + ('.' if pattern[change] == '#' else '#') + pattern[change + 1:]

        solution = find_ref(newpattern, val)
        if solution is not None:
            change_total += solution
            break
    else:
        print(pattern + '\n', val)
print(total)
print(change_total)
