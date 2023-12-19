import getinput

inp = getinput.fetchlines()


def p1(line):
    dr, dst, _ = line.split()
    dx, dy = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}[dr]
    dst = int(dst)
    return dx * dst, dy * dst


def p2(line):
    *_, info = line.split()
    dst = int(info[2:7], 16)
    dx, dy = [(1, 0), (0, -1), (-1, 0), (0, 1)][int(info[7])]
    return dx * dst, dy * dst


for f in [p1, p2]:
    x = y = mn = mx = 0
    colranges = set()
    rowranges = set()
    for line in inp:
        dx, dy = f(line)
        if dx:
            colranges.add((x, x + dx, y) if dx > 0 else (x + dx, x, y))
        else:
            rowranges.add((y, y + dy, x) if dy > 0 else (y + dy, y, x))
        x += dx
        y += dy
        mn, mx = min(mn, x), max(mx, x)
    print(colranges)
    total = 0
    for i in range(mn, mx + 1):
        edges = sorted((y, xs, xe) for xs, xe, y in colranges if xs <= i <= xe)
        j=0
        while j < len(edges) - 1:
            (y1, xs1, xe1), (y2, xs2, xe2) = edges[j:j+2]
            if xs1 == xe2 or xe1 == xs2:
                delete_2 = (y1 < y2) ^ (j % 2 > 0)
                del edges[j + delete_2]
            j += 1

        for j in range(len(edges) - 1):
            if j % 2 == 0:
                total += edges[j + 1][0] - edges[j][0] + 1
            elif (edges[j][0], edges[j+1][0], i) in rowranges:
                total += edges[j + 1][0] - edges[j][0] - 1

        #print(i, edges, total)
    print(total)

