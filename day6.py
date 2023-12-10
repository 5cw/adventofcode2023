inp = open('day6input.txt').readlines()
time, distance = [[int(t) for t in line.split(':')[1].split()] for line in inp]

prod = 1
for t, d in zip(time, distance):
    prod *= sum((t-i)*i > d for i in range(t))
print(prod)
bigt, bigd = [int(''.join(line.split(':')[1].split()))for line in inp]
print(sum((bigt-i)*i > bigd for i in range(bigt)))