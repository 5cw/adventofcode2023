import getinput, re, time, datetime
import sympy as sp
from decimal import Decimal

inp = getinput.fetchlines()

hailstones = [(*map(Decimal, re.split(r', | @', line)),) for line in inp]
print(hailstones)

MIN = 200000000000000
MAX = 400000000000000
hslines = []
for x, y, z, dx, dy, dz in hailstones:
    m = dy / dx
    b = y - x * m
    hslines.append((m, b))

total = 0

for i, (a, c) in enumerate(hslines):
    x, _, _, dx, _, _ = hailstones[i]
    for j, (b, d) in enumerate(hslines[i + 1:]):
        print(hailstones[i], a)
        print(hailstones[j + i + 1], b)
        if a == b:
            print('slopes\n')
            continue
        xi = (d - c) / (a - b)
        yi = a * xi + c
        u, _, _, du, _, _ = hailstones[j + i + 1]
        print(xi, yi, (xi - x) / dx, (xi - u) / du, '\n')
        if MIN <= xi <= MAX and MIN <= yi <= MAX and (xi - x) / dx >= 0 and (xi - u) / du >= 0:
            total += 1

hailstones = [(*map(int, p),) for p in hailstones]

NUM = 10

unknowns = sp.symbols("ox,oy,oz,odx,ody,odz")
ox, oy, oz, odx, ody, odz = unknowns
times = sp.symbols(','.join('x' + str(i) for i in range(NUM)))

eqs = []
for t, (x, y, z, dx, dy, dz) in zip(times, hailstones[:NUM]):
    eqs.extend([x - ox + dx*t - odx*t, y - oy + dy*t - ody*t, z - oz + dz*t - odz*t])

sols = sp.solve(eqs, unknowns+times, dict=True)[0]
print(sols)
print(sum(sols[n] for n in (ox,oy,oz)))

def move(n, pv):
    x, y, z, dx, dy, dz = pv
    return x + dx * n, y + dy * n, z + dz * n


CHECK_TO = 1000
inc = CHECK_TO / len(hailstones) ** 2

start = time.perf_counter_ns()


# coords = [(1, 4)]
def checkall(coords):
    for n, (i, j) in enumerate(coords):
        print(f'{i=}, {j=}')
        pct = 0
        now = time.perf_counter_ns()
        microseconds = (now - start) / 10 ** 3
        print('elapsed:', datetime.timedelta(microseconds=microseconds))
        print('est time remaining:',
              datetime.timedelta(microseconds=(microseconds / n) * (len(coords) - n)) if n else 0)
        for pv1 in hailstones:
            for pv2 in hailstones:
                x1, y1, z1 = move(i, pv1)
                x2, y2, z2 = move(j, pv2)
                d = j - i
                if not (x2 - x1) % d == (y2 - y1) % d == (z2 - z1) % d == 0:
                    continue
                dx = (x2 - x1) // d
                dy = (y2 - y1) // d
                dz = (z2 - z1) // d
                ox, oy, oz = x1 - dx * i, y1 - dy * i, z1 - dz * i

                for u, v, w, du, dv, dw in hailstones:
                    a, b, c, da, db, dc = u - ox, v - oy, w - oz, du - dx, dv - dy, dw - dz
                    k, *r = set(m / dm if dm else -m for m, dm in [(a, da), (b, db), (c, dc)])
                    if r or k % 1 > 0 or k < 0:
                        break
                else:
                    print(ox, oy, oz, ox + oy + oz)
                    return
# checkall(sorted([(i, j) for i in range(100, CHECK_TO) for j in range(i + 1, CHECK_TO)], key=sum))
