import getinput, re, math, dataclasses

inp = getinput.fetchlines()


@dataclasses.dataclass
class Point:
    x: int
    y: int
    z: int


@dataclasses.dataclass
class Brick:
    p1: Point
    p2: Point


bricks = []
for line in inp:
    s1, s2 = [map(int, s.split(',')) for s in line.split('~')]
    bricks.append(Brick(Point(*s1), Point(*s2)))
bricks.sort(key=lambda b: b.p1.z)
supportedby = []
for i, brick in enumerate(bricks):
    under = [(j, b2) for j, b2 in enumerate(bricks[:i]) if
             not (brick.p1.x > b2.p2.x
                  or brick.p2.x < b2.p1.x
                  or brick.p1.y > b2.p2.y
                  or brick.p2.y < b2.p1.y)]
    while brick.p1.z > 1 and all(brick.p1.z > b2.p2.z + 1 for _, b2 in under):
        brick.p1.z -= 1
        brick.p2.z -= 1
    supportedby.append([j for j, b2 in under if brick.p1.z == b2.p2.z + 1])

loadbearing = {j[0] for j in supportedby if len(j) == 1}
print(len(bricks) - len(loadbearing))

total = 0
for i, brick in enumerate(bricks):
    falling = {i}
    addition = True
    while addition:
        print(addition)
        addition = {j for j, l in enumerate(supportedby) if l and {*l} <= falling and j not in falling}
        falling |= addition
    total += len(falling) - 1
print(total)