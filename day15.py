import getinput
inp = getinput.fetch().strip().split(',')

def hash(string):
    total = 0
    for c in string:
        total = (total + ord(c))*17 % 256
    return total

print(sum(map(hash, inp)))

boxes = [[] for _ in range(256)]

for line in inp:
    if '=' in line:
        label, focal = line.split('=')
        box = hash(label)
        boxes[box] = [(l, f) if l != label else (label, focal) for l, f in boxes[box]]
        if (label, focal) not in boxes[box]:
            boxes[box].append((label, focal))
    else:
        label = line[:-1]
        box = hash(label)
        boxes[box] = [(l, f) for l, f in boxes[box] if l != label]

total = 0
for i, box in enumerate(boxes):
    for j, (_, focal) in enumerate(box):
        total += int(focal) * (i + 1) * (j + 1)

print(total)